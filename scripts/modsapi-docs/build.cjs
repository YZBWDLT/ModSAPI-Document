/* Build without sharing generated modules with the development server. */
const path = require('node:path');
const {spawnSync} = require('node:child_process');

const site = path.resolve(__dirname, '../..');
const cli = require.resolve('@docusaurus/core/bin/docusaurus.mjs', {paths: [site]});
const result = spawnSync(process.execPath, [cli, 'build', ...process.argv.slice(2)], {
  cwd: site,
  env: {
    ...process.env,
    DOCUSAURUS_GENERATED_FILES_DIR_NAME: process.env.DOCUSAURUS_GENERATED_FILES_DIR_NAME || '.docusaurus-build',
  },
  stdio: 'inherit',
});
if (result.error) throw result.error;
process.exitCode = result.status === null ? 1 : result.status;
