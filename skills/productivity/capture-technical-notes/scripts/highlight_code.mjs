const escapeHtml = (value) => value
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#39;");

const keywordSets = {
  swift: new Set([
    "actor", "any", "as", "associatedtype", "async", "await", "break", "case",
    "catch", "class", "continue", "convenience", "default", "defer", "deinit",
    "didSet", "do", "dynamic", "else", "enum", "extension", "fallthrough", "false",
    "fileprivate", "final", "for", "func", "get", "guard", "if", "import", "in",
    "indirect", "infix", "init", "inout", "internal", "is", "isolated", "lazy", "let",
    "mutating", "nil", "nonisolated", "open", "operator", "optional", "override", "postfix",
    "precedencegroup", "prefix", "private", "protocol", "public", "repeat", "required",
    "rethrows", "return", "self", "set", "some", "static", "struct", "subscript", "super",
    "switch", "throws", "throw", "true", "try", "typealias", "unowned", "var", "weak",
    "where", "while", "willSet",
  ]),
  javascript: new Set([
    "async", "await", "break", "case", "catch", "class", "const", "continue", "debugger",
    "default", "delete", "do", "else", "export", "extends", "false", "finally", "for",
    "from", "function", "get", "if", "import", "in", "instanceof", "let", "new", "null",
    "of", "return", "set", "static", "super", "switch", "this", "throw", "true", "try",
    "typeof", "undefined", "var", "void", "while", "with", "yield",
  ]),
  typescript: new Set([
    "abstract", "any", "as", "asserts", "async", "await", "boolean", "break", "case", "catch",
    "class", "const", "continue", "declare", "default", "delete", "do", "else", "enum",
    "export", "extends", "false", "finally", "for", "from", "function", "get", "if",
    "implements", "import", "in", "infer", "instanceof", "interface", "is", "keyof", "let",
    "namespace", "never", "new", "null", "number", "object", "of", "private", "protected",
    "public", "readonly", "return", "set", "static", "string", "super", "switch", "symbol",
    "this", "throw", "true", "try", "type", "typeof", "undefined", "unknown", "var", "void",
    "while", "with", "yield",
  ]),
  python: new Set([
    "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del",
    "elif", "else", "except", "False", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "raise", "return",
    "True", "try", "while", "with", "yield",
  ]),
  shell: new Set([
    "case", "do", "done", "elif", "else", "esac", "export", "fi", "for", "function", "if",
    "in", "local", "readonly", "select", "then", "until", "while",
  ]),
};

const aliases = new Map([
  ["bash", "shell"], ["sh", "shell"], ["zsh", "shell"],
  ["js", "javascript"], ["jsx", "javascript"],
  ["ts", "typescript"], ["tsx", "typescript"],
  ["py", "python"],
]);

const span = (kind, value) => `<span class="syntax-${kind}">${escapeHtml(value)}</span>`;

function readQuoted(code, start, quote, triple = false) {
  const delimiter = triple ? quote.repeat(3) : quote;
  let index = start + delimiter.length;
  while (index < code.length) {
    if (code.startsWith(delimiter, index)) return index + delimiter.length;
    if (!triple && code[index] === "\\") index += 2;
    else index += 1;
  }
  return code.length;
}

function readBlockComment(code, start) {
  let index = start + 2;
  let depth = 1;
  while (index < code.length && depth > 0) {
    if (code.startsWith("/*", index)) {
      depth += 1;
      index += 2;
    } else if (code.startsWith("*/", index)) {
      depth -= 1;
      index += 2;
    } else {
      index += 1;
    }
  }
  return index;
}

function nextNonWhitespace(code, index) {
  while (index < code.length && /\s/.test(code[index])) index += 1;
  return code[index] ?? "";
}

export function highlightCode(source, requestedLanguage = "") {
  const rawLanguage = requestedLanguage.toLowerCase().split(/\s+/)[0];
  const language = aliases.get(rawLanguage) ?? rawLanguage;
  const keywords = keywordSets[language]
    ?? (language === "json" ? new Set(["false", "null", "true"]) : null);
  if (!keywords) return escapeHtml(source);

  const parts = [];
  let index = 0;
  let previousWord = "";

  while (index < source.length) {
    const char = source[index];

    if (source.startsWith("//", index) && language !== "json") {
      const end = source.indexOf("\n", index);
      const stop = end === -1 ? source.length : end;
      parts.push(span("comment", source.slice(index, stop)));
      index = stop;
      continue;
    }
    if (source.startsWith("/*", index) && !["python", "shell", "json"].includes(language)) {
      const end = readBlockComment(source, index);
      parts.push(span("comment", source.slice(index, end)));
      index = end;
      continue;
    }
    if (char === "#" && ["python", "shell"].includes(language)) {
      const end = source.indexOf("\n", index);
      const stop = end === -1 ? source.length : end;
      parts.push(span("comment", source.slice(index, stop)));
      index = stop;
      continue;
    }

    if (language === "swift" && source.startsWith('"""', index)) {
      const end = readQuoted(source, index, '"', true);
      parts.push(span("string", source.slice(index, end)));
      index = end;
      continue;
    }
    if (char === '"' || char === "'" || (char === "`" && ["javascript", "typescript"].includes(language))) {
      const end = readQuoted(source, index, char);
      parts.push(span("string", source.slice(index, end)));
      index = end;
      continue;
    }

    const numberMatch = source.slice(index).match(/^(?:0[xob][0-9a-f_]+|\d(?:[\d_]*\d)?(?:\.\d(?:[\d_]*\d)?)?(?:e[+-]?\d+)?)/i);
    if (numberMatch) {
      parts.push(span("number", numberMatch[0]));
      index += numberMatch[0].length;
      previousWord = numberMatch[0];
      continue;
    }

    const directiveMatch = source.slice(index).match(/^#[A-Za-z_][A-Za-z0-9_]*/);
    if (directiveMatch) {
      parts.push(span("keyword", directiveMatch[0]));
      index += directiveMatch[0].length;
      previousWord = directiveMatch[0];
      continue;
    }

    const attributeMatch = source.slice(index).match(/^@[A-Za-z_][A-Za-z0-9_]*/);
    if (attributeMatch) {
      parts.push(span("type", attributeMatch[0]));
      index += attributeMatch[0].length;
      previousWord = attributeMatch[0];
      continue;
    }

    const identifierMatch = source.slice(index).match(/^[A-Za-z_][A-Za-z0-9_]*/);
    if (identifierMatch) {
      const word = identifierMatch[0];
      const after = nextNonWhitespace(source, index + word.length);
      const declaresType = ["actor", "class", "enum", "extension", "protocol", "struct", "typealias"].includes(previousWord);
      const isType = declaresType || /^[A-Z]/.test(word);
      const isCall = after === "(" && !keywords.has(word);
      if (keywords.has(word)) parts.push(span("keyword", word));
      else if (isType) parts.push(span("type", word));
      else if (isCall) parts.push(span("built_in", word));
      else parts.push(escapeHtml(word));
      index += word.length;
      previousWord = word;
      continue;
    }

    parts.push(escapeHtml(char));
    if (!/\s/.test(char) && !"@#$".includes(char)) previousWord = "";
    index += 1;
  }

  return parts.join("");
}

export function renderHighlightedCode(source, language = "") {
  const safeLanguage = language.toLowerCase().replace(/[^a-z0-9_+-]/g, "") || "text";
  const highlighted = highlightCode(source, safeLanguage);
  return `<pre class="code-listing"><code class="language-${safeLanguage} syntax-highlighted">${highlighted}</code></pre>`;
}
