-- Optional Supabase setup. Apply in your chosen academy project's SQL editor.
-- No existing remote database was changed during the build.
create table if not exists public.academy_progress (
 user_id uuid primary key references auth.users(id) on delete cascade,
 data jsonb not null default '{"completed":[],"attempts":[],"notes":{},"days":[]}'::jsonb,
 updated_at timestamptz not null default now()
);
alter table public.academy_progress enable row level security;
grant select, insert, update, delete on public.academy_progress to authenticated;
revoke all on public.academy_progress from anon;
create policy "Student reads own progress" on public.academy_progress for select to authenticated using ((select auth.uid()) = user_id);
create policy "Student creates own progress" on public.academy_progress for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "Student updates own progress" on public.academy_progress for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "Student deletes own progress" on public.academy_progress for delete to authenticated using ((select auth.uid()) = user_id);
