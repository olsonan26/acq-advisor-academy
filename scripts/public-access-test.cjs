const assert = require('node:assert/strict');
(async () => {
  const base = (process.env.ACADEMY_TEST_BASE_URL || 'http://127.0.0.1:3001').replace(/\/$/, '');
  const home = await fetch(base + '/', { redirect: 'manual' });
  assert.equal(home.status, 200, 'dashboard must load without redirect or password');
  console.log('PASS: public dashboard loads without sign-in');
  const practice = await fetch(base + '/api/practice', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mode: 'tutor', question: 'Explain gross profit' })
  });
  assert.equal(practice.status, 200, 'practice API must work without auth cookie');
  const data = await practice.json();
  assert.ok(typeof data.text === 'string' && data.text.length > 0);
  console.log('PASS: public practice API responds without sign-in');
  const oldAccess = await fetch(base + '/access', { redirect: 'manual' });
  assert.equal(oldAccess.status, 404, 'old password page should no longer exist');
  console.log('PASS: old password page is removed');
})().catch(e => { console.error(e); process.exitCode = 1; });
