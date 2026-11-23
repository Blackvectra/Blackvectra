#!/usr/bin/env node
// Fails if README.md links to a github.com page that does not answer 200.
// A repository that goes private, is renamed or never existed answers 404 to
// a visitor; that is how this profile once linked a repository that did not
// exist. Only github.com links are checked: mattlevorson.com sits behind
// Cloudflare bot protection, which answers 403 to any script, and its pages
// are checked by that site's own build.
import { readFile } from 'node:fs/promises';

const readme = await readFile(new URL('../README.md', import.meta.url), 'utf8');
const urls = [...new Set(readme.match(/https:\/\/github\.com\/[^\s)"'<>]+/g) ?? [])];

let failed = 0;
for (const url of urls) {
  let status;
  try {
    status = (await fetch(url, { redirect: 'follow', signal: AbortSignal.timeout(15000) })).status;
  } catch (err) {
    status = `request failed (${err.cause?.code ?? err.name})`;
  }
  if (status !== 200) failed++;
  console.log(`${status === 200 ? 'ok  ' : 'FAIL'} ${status} ${url}`);
}

if (urls.length === 0) {
  // An empty set would pass silently if the pattern ever stopped matching.
  console.error('check-repo-links: no github.com links found in README.md.');
  process.exit(1);
}
if (failed) {
  console.error(`check-repo-links: ${failed} of ${urls.length} link(s) do not answer 200.`);
  process.exit(1);
}
console.log(`check-repo-links: OK. ${urls.length} link(s).`);
