#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("manifest_tool.py")
SPEC = importlib.util.spec_from_file_location("manifest_tool", MODULE_PATH)
assert SPEC and SPEC.loader
manifest_tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(manifest_tool)


class ManifestToolTests(unittest.TestCase):
    def test_verified_manifest_and_tamper_detection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = root / "watch-manifest.json"
            frames = []
            png = base64.b64decode(
                "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
            )
            for index in range(11):
                frame = root / f"frame-{index}.png"
                frame.write_bytes(png + bytes([index]))
                frames.append(frame)

            init_args = argparse.Namespace(
                manifest=str(manifest_path),
                title="Test tutorial",
                source="https://example.com/tutorial",
                mode="browser",
                duration=30.0,
                width=960,
                height=540,
                transcript_source="site",
                force=False,
            )
            self.assertEqual(manifest_tool.init_manifest(init_args), 0)

            initial_observation_args = argparse.Namespace(
                manifest=str(manifest_path),
                timestamp=0.0,
                state="playing",
                duration=30.0,
                ready_state=4,
                width=960,
                height=540,
                notes="Observed the real player clock advance from the beginning.",
            )
            self.assertEqual(manifest_tool.add_observation(initial_observation_args), 0)

            checkpoint_specs = (
                (0.0, frames[0], "publication", "Section 1"),
                (7.0, frames[4], "boundary", "Section 1"),
                (10.0, frames[1], "publication", "Section 2"),
                (14.0, frames[5], "boundary", "Section 2"),
                (20.0, frames[2], "publication", "Section 3"),
                (22.0, frames[6], "boundary", "Section 3"),
                (29.0, frames[7], "boundary", "Section 4"),
                (30.0, frames[3], "audit", "Section 4"),
            )
            for index, (timestamp, frame, role, section) in enumerate(checkpoint_specs):
                checkpoint_args = argparse.Namespace(
                    manifest=str(manifest_path),
                    timestamp=timestamp,
                    frame=str(frame),
                    kind="slide",
                    description=f"Distinct slide layout visible at checkpoint {index}",
                    transcript_section=section,
                    note_anchor=section.lower().replace(" ", "-"),
                    capture_method="browser-rendered",
                    role=role,
                    discarded=False,
                )
                self.assertEqual(manifest_tool.add_checkpoint(checkpoint_args), 0)

                if timestamp == 10.0:
                    midpoint_observation_args = argparse.Namespace(
                        manifest=str(manifest_path),
                        timestamp=15.0,
                        state="seeked",
                        duration=30.0,
                        ready_state=4,
                        width=960,
                        height=540,
                        notes="Observed the rendered midpoint after a deterministic seek.",
                    )
                    self.assertEqual(
                        manifest_tool.add_observation(midpoint_observation_args), 0
                    )

            for index, (section_end, boundary_timestamp) in enumerate(
                ((7.5, 7.0), (15.0, 14.0), (22.5, 22.0), (30.0, 29.0))
            ):
                completion_args = argparse.Namespace(
                    manifest=str(manifest_path),
                    section=f"Section {index + 1}",
                    section_end=section_end,
                    boundary_timestamp=boundary_timestamp,
                    boundary_frame=str(frames[index + 4]),
                    knowledge_union="Completed slide title, labels, diagram, and footer are visible.",
                    publication_frame=[str(frames[min(index, 3)])],
                    result="pass",
                    notes="The selected publication frame covers the visible section-end union.",
                )
                self.assertEqual(
                    manifest_tool.add_section_completion(completion_args), 0
                )

            final_observation_args = argparse.Namespace(
                manifest=str(manifest_path),
                timestamp=30.0,
                state="paused",
                duration=30.0,
                ready_state=4,
                width=960,
                height=540,
                notes="Observed the completed final frame after the checkpoint pass.",
            )
            self.assertEqual(manifest_tool.add_observation(final_observation_args), 0)

            for index, timestamp in enumerate((3.0, 15.0, 27.0)):
                spot_args = argparse.Namespace(
                    manifest=str(manifest_path),
                    timestamp=timestamp,
                    frame=str(frames[index + 8]),
                    result="pass",
                    notes="Fresh capture confirmed the recorded visual state.",
                )
                self.assertEqual(manifest_tool.add_spot_check(spot_args), 0)

            finalize_args = argparse.Namespace(
                manifest=str(manifest_path),
                transcript_total=4,
                transcript_mapped=4,
                visual_events_total=3,
                visual_events_captured=3,
                max_gap_seconds=10.0,
                min_spot_checks=3,
                min_playback_observations=3,
            )
            self.assertEqual(manifest_tool.finalize_manifest(finalize_args), 0)
            validate_args = argparse.Namespace(manifest=str(manifest_path))
            self.assertEqual(manifest_tool.validate_manifest(validate_args), 0)

            valid_manifest = manifest_tool.read_json(manifest_path)
            reused_spot_manifest = copy.deepcopy(valid_manifest)
            reused_spot_manifest["spot_checks"][0]["frame_path"] = reused_spot_manifest[
                "checkpoints"
            ][0]["frame_path"]
            reused_spot_manifest["spot_checks"][0]["frame_sha256"] = reused_spot_manifest[
                "checkpoints"
            ][0]["frame_sha256"]
            manifest_tool.write_json(manifest_path, reused_spot_manifest)
            self.assertEqual(manifest_tool.validate_manifest(validate_args), 1)
            manifest_tool.write_json(manifest_path, valid_manifest)

            frames[0].write_bytes(b"tampered")
            self.assertEqual(manifest_tool.validate_manifest(validate_args), 1)


if __name__ == "__main__":
    unittest.main()
