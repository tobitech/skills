#!/usr/bin/env python3
"""Create and validate evidence manifests for tutorial-video notes."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
KINDS = ("slide", "slide-build", "demo", "code", "diagram", "talking-head", "other")
MODES = ("browser", "local", "downloaded")
CAPTURE_METHODS = ("browser-rendered", "local-frame")
CAPTURE_ROLES = ("audit", "publication", "boundary")
PLAYBACK_STATES = ("playing", "paused", "seeked")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def supported_image(path: Path) -> bool:
    with path.open("rb") as handle:
        header = handle.read(16)
    return (
        header.startswith(b"\x89PNG\r\n\x1a\n")
        or header.startswith(b"\xff\xd8\xff")
        or (header.startswith(b"RIFF") and header[8:12] == b"WEBP")
    )


def stored_path(manifest_path: Path, artifact_path: Path) -> str:
    artifact_path = artifact_path.resolve()
    try:
        return str(artifact_path.relative_to(manifest_path.parent.resolve()))
    except ValueError:
        return str(artifact_path)


def resolved_artifact(manifest_path: Path, value: str) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else manifest_path.parent / candidate


def new_manifest(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "created_at_utc": utc_now(),
        "updated_at_utc": utc_now(),
        "title": args.title,
        "source": {"value": args.source, "mode": args.mode},
        "media": {
            "duration_seconds": args.duration,
            "width": args.width,
            "height": args.height,
        },
        "transcript": {
            "source": args.transcript_source,
            "sections_total": 0,
            "sections_mapped": 0,
        },
        "checkpoints": [],
        "section_completion": [],
        "playback_observations": [],
        "spot_checks": [],
        "visual_events": {"total": 0, "captured": 0},
        "coverage": {},
        "verification": {"status": "draft", "reasons": []},
    }


def init_manifest(args: argparse.Namespace) -> int:
    path = Path(args.manifest).resolve()
    if path.exists() and not args.force:
        raise ValueError(f"Manifest already exists: {path}. Pass --force to replace it.")
    write_json(path, new_manifest(args))
    print(path)
    return 0


def add_checkpoint(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    frame_path = Path(args.frame).resolve()
    if not frame_path.is_file():
        raise ValueError(f"Frame does not exist: {frame_path}")
    manifest = read_json(manifest_path)
    checkpoints = manifest.setdefault("checkpoints", [])
    checkpoint = {
        "id": f"cp-{len(checkpoints) + 1:05d}",
        "timestamp_seconds": args.timestamp,
        "observed_at_utc": utc_now(),
        "frame_path": stored_path(manifest_path, frame_path),
        "frame_sha256": sha256(frame_path),
        "kind": args.kind,
        "description": args.description.strip(),
        "transcript_section": args.transcript_section.strip(),
        "note_anchor": args.note_anchor.strip(),
        "capture_method": args.capture_method,
        "capture_role": getattr(args, "role", "audit"),
        "retained": not args.discarded,
    }
    checkpoints.append(checkpoint)
    manifest["updated_at_utc"] = utc_now()
    manifest["verification"] = {"status": "draft", "reasons": []}
    write_json(manifest_path, manifest)
    print(checkpoint["id"])
    return 0


def add_section_completion(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    boundary_path = Path(args.boundary_frame).resolve()
    publication_paths = [Path(value).resolve() for value in args.publication_frame]
    for frame in [boundary_path, *publication_paths]:
        if not frame.is_file():
            raise ValueError(f"Completion-matrix frame does not exist: {frame}")
    manifest = read_json(manifest_path)
    rows = manifest.setdefault("section_completion", [])
    row = {
        "id": f"completion-{len(rows) + 1:03d}",
        "section": args.section.strip(),
        "section_end_seconds": args.section_end,
        "boundary_timestamp_seconds": args.boundary_timestamp,
        "boundary_frame_path": stored_path(manifest_path, boundary_path),
        "boundary_frame_sha256": sha256(boundary_path),
        "visible_knowledge_union": args.knowledge_union.strip(),
        "publication_frames": [
            {
                "frame_path": stored_path(manifest_path, frame),
                "frame_sha256": sha256(frame),
            }
            for frame in publication_paths
        ],
        "result": args.result,
        "notes": args.notes.strip(),
        "observed_at_utc": utc_now(),
    }
    rows.append(row)
    manifest["updated_at_utc"] = utc_now()
    manifest["verification"] = {"status": "draft", "reasons": []}
    write_json(manifest_path, manifest)
    print(row["id"])
    return 0


def add_observation(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    manifest = read_json(manifest_path)
    observations = manifest.setdefault("playback_observations", [])
    observation = {
        "id": f"obs-{len(observations) + 1:04d}",
        "observed_at_utc": utc_now(),
        "player_time_seconds": args.timestamp,
        "playback_state": args.state,
        "duration_seconds": args.duration,
        "ready_state": args.ready_state,
        "width": args.width,
        "height": args.height,
        "notes": args.notes.strip(),
    }
    observations.append(observation)
    manifest["updated_at_utc"] = utc_now()
    manifest["verification"] = {"status": "draft", "reasons": []}
    write_json(manifest_path, manifest)
    print(observation["id"])
    return 0


def add_spot_check(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    frame_path = Path(args.frame).resolve()
    if not frame_path.is_file():
        raise ValueError(f"Spot-check frame does not exist: {frame_path}")
    manifest = read_json(manifest_path)
    checks = manifest.setdefault("spot_checks", [])
    check = {
        "id": f"spot-{len(checks) + 1:03d}",
        "timestamp_seconds": args.timestamp,
        "observed_at_utc": utc_now(),
        "frame_path": stored_path(manifest_path, frame_path),
        "frame_sha256": sha256(frame_path),
        "result": args.result,
        "notes": args.notes.strip(),
    }
    checks.append(check)
    manifest["updated_at_utc"] = utc_now()
    manifest["verification"] = {"status": "draft", "reasons": []}
    write_json(manifest_path, manifest)
    print(check["id"])
    return 0


def union_coverage_ratio(times: list[float], duration: float, radius: float) -> float:
    if not times or duration <= 0:
        return 0.0
    intervals = sorted((max(0.0, t - radius), min(duration, t + radius)) for t in times)
    total = 0.0
    start, end = intervals[0]
    for next_start, next_end in intervals[1:]:
        if next_start <= end:
            end = max(end, next_end)
        else:
            total += end - start
            start, end = next_start, next_end
    total += end - start
    return min(1.0, total / duration)


def evidence_errors(manifest_path: Path, manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append("Unsupported or missing schema_version.")
    for collection in ("checkpoints", "spot_checks"):
        for item in manifest.get(collection, []):
            frame_value = item.get("frame_path", "")
            frame = resolved_artifact(manifest_path, frame_value) if frame_value else None
            if frame is None or not frame.is_file():
                errors.append(f"{item.get('id', collection)} is missing its evidence frame.")
            elif not supported_image(frame):
                errors.append(f"{item.get('id', collection)} evidence is not PNG, JPEG, or WebP.")
            elif sha256(frame) != item.get("frame_sha256"):
                errors.append(f"{item.get('id', collection)} frame hash does not match.")
    for row in manifest.get("section_completion", []):
        boundary_value = row.get("boundary_frame_path", "")
        boundary = resolved_artifact(manifest_path, boundary_value) if boundary_value else None
        if boundary is None or not boundary.is_file():
            errors.append(f"{row.get('id', 'completion')} is missing its boundary frame.")
        elif not supported_image(boundary):
            errors.append(f"{row.get('id', 'completion')} boundary evidence is not PNG, JPEG, or WebP.")
        elif sha256(boundary) != row.get("boundary_frame_sha256"):
            errors.append(f"{row.get('id', 'completion')} boundary frame hash does not match.")
        for index, item in enumerate(row.get("publication_frames", []), start=1):
            value = item.get("frame_path", "")
            frame = resolved_artifact(manifest_path, value) if value else None
            if frame is None or not frame.is_file():
                errors.append(
                    f"{row.get('id', 'completion')} publication frame {index} is missing."
                )
            elif not supported_image(frame):
                errors.append(
                    f"{row.get('id', 'completion')} publication frame {index} is not PNG, JPEG, or WebP."
                )
            elif sha256(frame) != item.get("frame_sha256"):
                errors.append(
                    f"{row.get('id', 'completion')} publication frame {index} hash does not match."
                )
    return errors


def verification_evaluation(
    manifest_path: Path,
    manifest: dict[str, Any],
    max_gap_seconds: float,
    min_spot_checks: int,
    min_playback_observations: int,
) -> tuple[list[str], dict[str, Any]]:
    reasons = evidence_errors(manifest_path, manifest)
    duration = float(manifest.get("media", {}).get("duration_seconds") or 0)
    retained = [c for c in manifest.get("checkpoints", []) if c.get("retained", True)]
    capture_order_times = [float(c.get("timestamp_seconds", 0)) for c in retained]
    times = sorted(capture_order_times)

    if duration <= 0:
        reasons.append("Video duration is unknown or zero.")
    if not retained:
        reasons.append("No retained visual checkpoints exist.")
    if any(b < a for a, b in zip(capture_order_times, capture_order_times[1:])):
        reasons.append("Initial visual checkpoints are not in monotonic playback order.")
    if duration > 0 and any(t < 0 or t > duration for t in times):
        reasons.append("One or more checkpoint timestamps are outside the video duration.")

    observations = manifest.get("playback_observations", [])
    observation_times = [float(item.get("player_time_seconds", 0)) for item in observations]
    if len(observations) < min_playback_observations:
        reasons.append(
            f"Only {len(observations)}/{min_playback_observations} required playback observations exist."
        )
    if any(b < a for a, b in zip(observation_times, observation_times[1:])):
        reasons.append("Playback observations are not in monotonic timeline order.")
    if duration > 0 and observation_times:
        if observation_times[0] > max_gap_seconds:
            reasons.append("Playback telemetry does not cover the beginning of the video.")
        if duration - observation_times[-1] > max_gap_seconds:
            reasons.append("Playback telemetry does not cover the end of the video.")
        if any(t < 0 or t > duration for t in observation_times):
            reasons.append("A playback observation is outside the video duration.")
    if observations and not any(item.get("playback_state") == "playing" for item in observations):
        reasons.append("No playback observation recorded a playing state.")

    checkpoint_record_times = [str(item.get("observed_at_utc", "")) for item in retained]
    observation_record_times = [str(item.get("observed_at_utc", "")) for item in observations]
    if retained and observations and checkpoint_record_times and observation_record_times:
        first_checkpoint_record = min(checkpoint_record_times)
        last_checkpoint_record = max(checkpoint_record_times)
        if min(observation_record_times) > first_checkpoint_record:
            reasons.append("No playback telemetry was recorded before the first checkpoint batch.")
        if max(observation_record_times) < last_checkpoint_record:
            reasons.append("No playback telemetry was recorded after the final checkpoint batch.")
        if len(retained) > 1 and not any(
            first_checkpoint_record <= value <= last_checkpoint_record
            for value in observation_record_times
        ):
            reasons.append("No playback telemetry was recorded during checkpoint capture.")
    for observation in observations:
        observed_duration = float(observation.get("duration_seconds") or 0)
        if duration > 0 and abs(observed_duration - duration) > 1.0:
            reasons.append(f"{observation.get('id')} reports an inconsistent video duration.")
        if int(observation.get("ready_state") or 0) < 2:
            reasons.append(f"{observation.get('id')} reports insufficient media readiness.")
        if int(observation.get("width") or 0) <= 0 or int(observation.get("height") or 0) <= 0:
            reasons.append(f"{observation.get('id')} lacks valid video dimensions.")
        if len(str(observation.get("notes", "")).strip()) < 8:
            reasons.append(f"{observation.get('id')} lacks an observation note.")

    timeline_gaps: list[float] = []
    if times and duration > 0:
        timeline_gaps = [times[0]]
        timeline_gaps.extend(b - a for a, b in zip(times, times[1:]))
        timeline_gaps.append(max(0.0, duration - times[-1]))
    max_observed_gap = max(timeline_gaps, default=duration)
    if duration > 0 and max_observed_gap > max_gap_seconds:
        reasons.append(
            f"Maximum checkpoint gap {max_observed_gap:.3f}s exceeds {max_gap_seconds:.3f}s."
        )

    for checkpoint in retained:
        if checkpoint.get("kind") not in KINDS:
            reasons.append(f"{checkpoint.get('id')} has an invalid visual kind.")
        if checkpoint.get("capture_method") not in CAPTURE_METHODS:
            reasons.append(f"{checkpoint.get('id')} has an invalid capture method.")
        if checkpoint.get("capture_role", "audit") not in CAPTURE_ROLES:
            reasons.append(f"{checkpoint.get('id')} has an invalid capture role.")
        if len(str(checkpoint.get("description", "")).strip()) < 12:
            reasons.append(f"{checkpoint.get('id')} lacks a substantive visual description.")
        if not str(checkpoint.get("transcript_section", "")).strip():
            reasons.append(f"{checkpoint.get('id')} is not mapped to a transcript section.")

    transcript = manifest.get("transcript", {})
    transcript_total = int(transcript.get("sections_total") or 0)
    transcript_mapped = int(transcript.get("sections_mapped") or 0)
    if transcript_total <= 0:
        reasons.append("No transcript sections were counted.")
    elif transcript_mapped != transcript_total:
        reasons.append(f"Transcript mapping is incomplete: {transcript_mapped}/{transcript_total}.")

    completion_rows = manifest.get("section_completion", [])
    if transcript_total > 0 and len(completion_rows) != transcript_total:
        reasons.append(
            f"Section-boundary completion matrix is incomplete: {len(completion_rows)}/{transcript_total}."
        )
    boundary_checkpoints = [
        checkpoint
        for checkpoint in retained
        if checkpoint.get("capture_role", "audit") == "boundary"
    ]
    if transcript_total > 0 and len(boundary_checkpoints) < transcript_total:
        reasons.append(
            f"Only {len(boundary_checkpoints)}/{transcript_total} required boundary checkpoints exist."
        )
    seen_completion_sections: set[str] = set()
    for row in completion_rows:
        row_id = row.get("id", "completion")
        section = str(row.get("section", "")).strip()
        if not section:
            reasons.append(f"{row_id} has no transcript section.")
        elif section in seen_completion_sections:
            reasons.append(f"{row_id} duplicates completion section {section}.")
        seen_completion_sections.add(section)
        section_end = float(row.get("section_end_seconds") or 0)
        boundary_time = float(row.get("boundary_timestamp_seconds") or 0)
        if section_end <= 0 or boundary_time < 0 or abs(section_end - boundary_time) > 2.1:
            reasons.append(f"{row_id} does not contain a boundary probe within roughly two seconds of section end.")
        if len(str(row.get("visible_knowledge_union", "")).strip()) < 12:
            reasons.append(f"{row_id} lacks a substantive visible-knowledge union.")
        if not row.get("publication_frames"):
            reasons.append(f"{row_id} has no selected publication frame.")
        if row.get("result") != "pass":
            reasons.append(f"{row_id} does not pass its section-boundary completion review.")

    visual_events = manifest.get("visual_events", {})
    visual_total = int(visual_events.get("total") or 0)
    visual_captured = int(visual_events.get("captured") or 0)
    if visual_total < 0 or visual_captured < 0:
        reasons.append("Visual-event counts cannot be negative.")
    elif visual_captured != visual_total:
        reasons.append(f"Visual-event capture is incomplete: {visual_captured}/{visual_total}.")

    audit_checkpoints = sum(
        1 for checkpoint in retained if checkpoint.get("capture_role", "audit") == "audit"
    )
    publication_checkpoints = sum(
        1 for checkpoint in retained if checkpoint.get("capture_role", "audit") == "publication"
    )
    classified_checkpoints = sum(1 for checkpoint in retained if checkpoint.get("kind") != "other")
    if visual_total > 0 and publication_checkpoints < visual_total:
        reasons.append(
            f"Only {publication_checkpoints}/{visual_total} significant visual events have publication checkpoints."
        )
    if visual_total > 0 and classified_checkpoints < visual_total:
        reasons.append(
            f"Only {classified_checkpoints}/{visual_total} significant visual events have a specific visual classification."
        )
    if visual_total > 0 and audit_checkpoints == 0:
        reasons.append("No audit-role checkpoints preserve the coverage sweep.")

    spot_checks = manifest.get("spot_checks", [])
    passed_spots = sum(1 for check in spot_checks if check.get("result") == "pass")
    failed_spots = sum(1 for check in spot_checks if check.get("result") == "fail")
    if passed_spots < min_spot_checks:
        reasons.append(f"Only {passed_spots}/{min_spot_checks} required spot checks passed.")
    if failed_spots:
        reasons.append(f"{failed_spots} spot check(s) failed.")
    retained_hashes = {str(checkpoint.get("frame_sha256", "")) for checkpoint in retained}
    for check in spot_checks:
        if str(check.get("frame_sha256", "")) in retained_hashes:
            reasons.append(
                f"{check.get('id')} reuses a checkpoint frame instead of an independent fresh capture."
            )
    if retained and spot_checks:
        last_checkpoint_record = max(checkpoint_record_times)
        if any(str(check.get("observed_at_utc", "")) <= last_checkpoint_record for check in spot_checks):
            reasons.append("One or more spot checks were recorded before checkpoint capture finished.")
    passed_spot_times = sorted(
        float(check.get("timestamp_seconds", 0))
        for check in spot_checks
        if check.get("result") == "pass"
    )
    if duration > 0 and len(passed_spot_times) >= min_spot_checks:
        if passed_spot_times[0] > duration / 3:
            reasons.append("No passing spot check covers the beginning third of the video.")
        if not any(duration / 3 <= value <= 2 * duration / 3 for value in passed_spot_times):
            reasons.append("No passing spot check covers the middle third of the video.")
        if passed_spot_times[-1] < 2 * duration / 3:
            reasons.append("No passing spot check covers the ending third of the video.")

    transcript_ratio = transcript_mapped / transcript_total if transcript_total > 0 else 0.0
    visual_ratio = visual_captured / visual_total if visual_total > 0 else 1.0
    coverage = {
        "timeline_ratio": round(
            union_coverage_ratio(times, duration, max_gap_seconds / 2), 6
        ),
        "maximum_checkpoint_gap_seconds": round(max_observed_gap, 6),
        "transcript_ratio": round(transcript_ratio, 6),
        "visual_event_ratio": round(visual_ratio, 6),
        "spot_checks_passed": passed_spots,
        "spot_checks_total": len(spot_checks),
        "playback_observations": len(observations),
        "audit_checkpoints": audit_checkpoints,
        "publication_checkpoints": publication_checkpoints,
        "boundary_checkpoints": len(boundary_checkpoints),
        "section_completion_rows": len(completion_rows),
        "playback_span_ratio": round(
            (max(observation_times) - min(observation_times)) / duration
            if duration > 0 and observation_times
            else 0.0,
            6,
        ),
    }
    return reasons, coverage


def finalize_manifest(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    manifest = read_json(manifest_path)
    manifest["transcript"] = {
        **manifest.get("transcript", {}),
        "sections_total": args.transcript_total,
        "sections_mapped": args.transcript_mapped,
    }
    manifest["visual_events"] = {
        "total": args.visual_events_total,
        "captured": args.visual_events_captured,
    }

    reasons, coverage = verification_evaluation(
        manifest_path,
        manifest,
        args.max_gap_seconds,
        args.min_spot_checks,
        args.min_playback_observations,
    )
    manifest["coverage"] = coverage
    manifest["verification"] = {
        "status": "verified" if not reasons else "unverified",
        "evaluated_at_utc": utc_now(),
        "criteria": {
            "max_gap_seconds": args.max_gap_seconds,
            "min_spot_checks": args.min_spot_checks,
            "min_playback_observations": args.min_playback_observations,
        },
        "reasons": reasons,
    }
    manifest["updated_at_utc"] = utc_now()
    write_json(manifest_path, manifest)
    print(json.dumps({"status": manifest["verification"]["status"], "reasons": reasons}, indent=2))
    return 0 if not reasons else 1


def validate_manifest(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    manifest = read_json(manifest_path)
    verification = manifest.get("verification", {})
    criteria = verification.get("criteria", {})
    errors, coverage = verification_evaluation(
        manifest_path,
        manifest,
        float(criteria.get("max_gap_seconds", 10.0)),
        int(criteria.get("min_spot_checks", 3)),
        int(criteria.get("min_playback_observations", 3)),
    )
    status = verification.get("status", "draft")
    if status != "verified":
        errors.append(f"Stored manifest verdict is {status}, not verified.")
    result = {
        "status": "verified" if not errors else "unverified",
        "coverage": coverage,
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


def doctor(args: argparse.Namespace) -> int:
    tools = {name: shutil.which(name) for name in ("ffmpeg", "ffprobe", "yt-dlp")}
    result = {
        "browser_mode_ready": True,
        "local_mode_ready": bool(tools["ffmpeg"] and tools["ffprobe"]),
        "download_mode_ready": bool(tools["yt-dlp"] and tools["ffmpeg"] and tools["ffprobe"]),
        "tools": tools,
    }
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor_parser = subparsers.add_parser("doctor", help="Report optional local-tool readiness.")
    doctor_parser.set_defaults(handler=doctor)

    init_parser = subparsers.add_parser("init", help="Create a draft evidence manifest.")
    init_parser.add_argument("--manifest", required=True)
    init_parser.add_argument("--title", required=True)
    init_parser.add_argument("--source", required=True)
    init_parser.add_argument("--mode", choices=MODES, required=True)
    init_parser.add_argument("--duration", type=float, required=True)
    init_parser.add_argument("--width", type=int, default=0)
    init_parser.add_argument("--height", type=int, default=0)
    init_parser.add_argument(
        "--transcript-source", choices=("site", "captions", "asr", "none"), default="none"
    )
    init_parser.add_argument("--force", action="store_true")
    init_parser.set_defaults(handler=init_manifest)

    checkpoint_parser = subparsers.add_parser("add-checkpoint", help="Record a visual checkpoint.")
    checkpoint_parser.add_argument("--manifest", required=True)
    checkpoint_parser.add_argument("--timestamp", type=float, required=True)
    checkpoint_parser.add_argument("--frame", required=True)
    checkpoint_parser.add_argument("--kind", choices=KINDS, required=True)
    checkpoint_parser.add_argument("--description", required=True)
    checkpoint_parser.add_argument("--transcript-section", required=True)
    checkpoint_parser.add_argument("--note-anchor", default="")
    checkpoint_parser.add_argument(
        "--capture-method", choices=CAPTURE_METHODS, required=True
    )
    checkpoint_parser.add_argument("--role", choices=CAPTURE_ROLES, default="audit")
    checkpoint_parser.add_argument("--discarded", action="store_true")
    checkpoint_parser.set_defaults(handler=add_checkpoint)

    completion_parser = subparsers.add_parser(
        "add-section-completion",
        help="Record a section-end boundary probe and its publication-frame union.",
    )
    completion_parser.add_argument("--manifest", required=True)
    completion_parser.add_argument("--section", required=True)
    completion_parser.add_argument("--section-end", type=float, required=True)
    completion_parser.add_argument("--boundary-timestamp", type=float, required=True)
    completion_parser.add_argument("--boundary-frame", required=True)
    completion_parser.add_argument("--knowledge-union", required=True)
    completion_parser.add_argument("--publication-frame", action="append", required=True)
    completion_parser.add_argument("--result", choices=("pass", "fail"), required=True)
    completion_parser.add_argument("--notes", required=True)
    completion_parser.set_defaults(handler=add_section_completion)

    observation_parser = subparsers.add_parser(
        "add-observation", help="Record raw player telemetry."
    )
    observation_parser.add_argument("--manifest", required=True)
    observation_parser.add_argument("--timestamp", type=float, required=True)
    observation_parser.add_argument("--state", choices=PLAYBACK_STATES, required=True)
    observation_parser.add_argument("--duration", type=float, required=True)
    observation_parser.add_argument("--ready-state", type=int, required=True)
    observation_parser.add_argument("--width", type=int, required=True)
    observation_parser.add_argument("--height", type=int, required=True)
    observation_parser.add_argument("--notes", required=True)
    observation_parser.set_defaults(handler=add_observation)

    spot_parser = subparsers.add_parser("add-spot-check", help="Record an independent spot check.")
    spot_parser.add_argument("--manifest", required=True)
    spot_parser.add_argument("--timestamp", type=float, required=True)
    spot_parser.add_argument("--frame", required=True)
    spot_parser.add_argument("--result", choices=("pass", "fail"), required=True)
    spot_parser.add_argument("--notes", required=True)
    spot_parser.set_defaults(handler=add_spot_check)

    finalize_parser = subparsers.add_parser("finalize", help="Evaluate coverage and set a verdict.")
    finalize_parser.add_argument("--manifest", required=True)
    finalize_parser.add_argument("--transcript-total", type=int, required=True)
    finalize_parser.add_argument("--transcript-mapped", type=int, required=True)
    finalize_parser.add_argument("--visual-events-total", type=int, required=True)
    finalize_parser.add_argument("--visual-events-captured", type=int, required=True)
    finalize_parser.add_argument("--max-gap-seconds", type=float, default=10.0)
    finalize_parser.add_argument("--min-spot-checks", type=int, default=3)
    finalize_parser.add_argument("--min-playback-observations", type=int, default=3)
    finalize_parser.set_defaults(handler=finalize_manifest)

    validate_parser = subparsers.add_parser("validate", help="Validate evidence files and verdict.")
    validate_parser.add_argument("--manifest", required=True)
    validate_parser.set_defaults(handler=validate_manifest)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.handler(args))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
