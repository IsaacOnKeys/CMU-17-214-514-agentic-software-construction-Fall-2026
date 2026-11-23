"""Build the initial reconstructed course package. No exercise or cloud execution.

Run from the workspace with Python + openpyxl. Rebuild preserves tracked progress
by stable IDs; inspect proposed curriculum changes before using it after study begins.
"""
from pathlib import Path
from html import unescape
import argparse
import json
import re
from urllib.parse import quote
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.comments import Comment
from course_data import FALL, SPRING, SITE, LECTURES, LABS, HWS, EXTERNAL

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx'
HEADERS = ['Order', 'ID', 'Activity type', 'Topic / action', 'Learning objective',
           'Core resources', 'Supplementary resources', 'Dependencies', 'Trigger',
           'Saved prompt', 'Expected output', 'Done when', 'Status / Complete',
           'Evidence / output link', 'Notes']
rows = []
prompts = []
id_path = ROOT / 'prompts/task-id-map.json'
id_map = json.loads(id_path.read_text(encoding='utf-8')) if id_path.exists() else {}
resources = []
override_path = ROOT / 'curriculum/source-link-overrides.json'
SOURCE_LINK_OVERRIDES = json.loads(override_path.read_text(encoding='utf-8')) if override_path.exists() else {}


def resolve_source_links(text):
    for original, replacement in SOURCE_LINK_OVERRIDES.items():
        text = text.replace(original, replacement)
    # Raw Markdown has no rendered GitHub heading anchors; the named section is in the row title/text.
    text = re.sub(r'(https://raw\.githubusercontent\.com/[^\s)<>`"|]+\.md)#[a-z0-9-]+', r'\1', text)
    return text


def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(resolve_source_links(text).rstrip()+'\n', encoding='utf-8')


def slug(text):
    return re.sub('[^a-z0-9]+', '-', text.lower()).strip('-')


def source(path):
    return resolve_source_links(FALL + path)


def spring_links():
    text = (ROOT / 'course-materials/s2026/README.md').read_text(encoding='utf-8')
    return {unescape(re.sub('<[^>]+>', '', title)): url for url, title in
            re.findall(r'<a href="(https://docs.google.com/presentation/[^\"]+)"[^>]*>(.*?)</a>', text)}


SPRING_DECKS = spring_links()


def add(rid, kind, title, objective, core, output, done, *, deps=None, trigger=None, supplement='', notes='', prompt=''):
    # The explicit predecessor chain makes every operational gate visible and prevents silent skips.
    core, supplement = resolve_source_links(core), resolve_source_links(supplement)
    dep_ids = deps if deps is not None else ([rows[-1]['ID']] if rows else [])
    row = dict(zip(HEADERS, [len(rows)+1, rid, kind, title, objective, core, supplement,
                            ', '.join(dep_ids), trigger or 'After dependencies are complete; before the next row',
                            prompt, output, done, 'Ready' if not rows else 'Not started', '', notes]))
    rows.append(row)
    return rid


COMMON_CONSTRAINTS = '''Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.'''

CLOUD_CONTROLS = '''Before any AWS mutation, verify the selected profile and region with explicit CLI flags and `aws sts get-caller-identity`; record a redacted account identifier, role and region, never credentials. Do not silently use the default profile. Inspect the exact template/plan and estimate current regional instance, EBS, public IPv4, storage, registry, telemetry, network and data-transfer exposure with AWS pricing sources. Set a learner-approved spend limit, duration and budget alerts; alerts and a stop timer are not hard billing caps. Tag and inventory every created resource in `progress/cloud-resources.md`, link this task to its named teardown row, and choose a minimal design without an unnecessary NAT gateway. A personal account has neither Academy's $50 enforcement nor automatic session cleanup. Preserve evidence before deletion. Before destructive teardown present exact account/region/resource IDs and obtain approval; delete only the approved inventory and verify resources, retained disks, addresses, logs and storage that can still incur costs.'''


def jit(key, title, objective, core, inputs, steps, outputs, done, *, kind='JIT preparation', supplement='', notes='', trigger=None, cloud=False):
    if key not in id_map:
        id_map[key] = 'JIT-'+str(max([int(v[4:]) for v in id_map.values()] or [0])+1).zfill(3)
    rid = id_map[key]
    filename = f'prompts/{rid}-{slug(key)}.md'
    deps = [rows[-1]['ID']] if rows else []
    when = trigger or f'After {deps[0] if deps else "opening the workbook"}; execute this row before the next activity.'
    add(rid,kind,title,objective,core,outputs,done,deps=deps,trigger=when,supplement=supplement,notes=notes,prompt='../'+filename)
    body = f'''# {rid}: {title}

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **{title}**. Its objective is: {objective}

Authoritative course source: {core}

Supporting resource: {supplement or 'Use the source and the specific local artifacts below; do not add unrelated preparation.'}

Workspace: `E:\\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `{rid}`.

## When to run

{when}

Required completed queue rows: {', '.join(deps) or 'none'}. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

{inputs}

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

'''+ '\n'.join(f'{i}. {step}' for i, step in enumerate(steps,1))+f'''

## Constraints

{COMMON_CONSTRAINTS}

{CLOUD_CONTROLS if cloud else 'This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.'}

## Outputs and progress

{outputs}

Write the evidence record to `reviews/{rid}.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `{rid}` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **{done}**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
'''
    write(filename,body)
    prompts.append(dict(id=rid,row=rid,key=key,file=filename,trigger=when,purpose=title,output=outputs))
    return rid


def lecture(n):
    data = LECTURES[n-1]
    code,title,objective,pages,example,prereq,gap,spring,question = data
    supp = SPRING_DECKS.get(spring, '')
    add(f'LEC-{n:02}', 'Lecture', title, objective, source(f'slides/{code}.pdf'),
        f'notes/LEC-{n:02}.md: terms, source-page citations, example explanation, unassisted answer and open questions',
        f'Read the deck and explain its example in your own words. Answer: {question} Record remaining questions; this is self-study recall, not an official quiz.',
        supplement=supp,notes=f'Original CMU PDF; focal pages {pages}. Prerequisites: {prereq} {gap}')


def supplement(rid,title,objective,url,done,notes=''):
    add(rid,'Supplementary study',title,objective,url,f'notes/{rid}.md with the requested explanation or a justified prerequisite waiver',done,notes=notes)


def lab(n):
    d = LABS[n-1]
    unit = f'lab{n:02}'
    core = source(f'labs/{unit}.md') if n<13 else SITE+'#schedule'
    starter = f'https://github.com/CMU-17-214/f26-{unit}' if n<13 else SITE+'#schedule'
    if n==13:
        refresh('lab13','Lab 13 handout and starter','No official Lab 13 handout/repo link in the pinned snapshot. If still absent, reconstruct a minimal three-milestone observability exercise from the published title and HW6 telemetry obligations, label its objectives inferred and freeze it before setup.')
    common_inputs = f'Current unit metadata in `labs/{unit}/LOCATION.md`; source handout {core}; public starter {starter}; {d["files"]}. Tools needed now: {d["tools"]}. Expected baseline: {d["baseline"]}. {d["boundaries"]}'
    jit(f'{unit}-prepare',f'Prepare Lab {n:02}: {d["title"]}',d['objective'],core,common_inputs,
        [f'Read the complete handout and SETUP.md for Lab {n:02}; inspect only its build manifests, CI and named input files. Record the pinned public starter SHA from source-manifest.json.',
         f'Create an isolated working copy at `labs/{unit}/work/` or record the learner-selected repository in LOCATION.md; use the pristine archived starter, not a previous lab solution. Track adaptation diffs separately. If a public fork/Actions evidence is required, prepare it locally first and obtain explicit authorization before publishing the fork or workflow.',
         f'Install only {d["tools"]}. Follow the pinned setup/lockfiles. On Windows translate virtual-environment paths and Java classpath separators, or use the learner’s existing WSL environment; do not require WSL for all labs.',
         f'Check presence of {d["files"]}. {d["boundaries"]}',
         ('Produce an adapted Lab 4 template and account/runbook diff, keeping the original untouched; separate cloud readiness/provisioning rows govern resource creation.' if n==4 else 'No cloud configuration is needed for this lab; preserve the current repository and staged discovery order.')],
        f'`labs/{unit}/LOCATION.md`, `labs/{unit}/preparation.md`, baseline SHA, adaptation diff if any; dependencies installed only for this lab',
        f'Lab {n:02} input files and current-unit tools exist, provenance is recorded, and no exercise behavior or solution was changed.',supplement=starter)
    jit(f'{unit}-preflight',f'Verify Lab {n:02} starter health',d['objective'],core,common_inputs+f' Read `labs/{unit}/preparation.md` and the working-tree diff.',
        [f'From the recorded Lab {n:02} working copy, run only this preflight: {d["check"]}. Capture complete command/result and test-discovery counts; distinguish compile/dependency failures from intended behavior.',
         f'Compare against this documented baseline: {d["baseline"]}',
         f'Check the working diff and scope boundaries: {d["boundaries"]}',
         'If the baseline differs, record the exact runtime/source revision and investigate environment or source drift. Do not repair intended exercise failures or claim readiness from static inspection.'],
        f'`labs/{unit}/preflight.md` with commands, exit codes, expected/observed counts, source SHA and readiness verdict',
        d['baseline'],kind='JIT verification',supplement=starter)
    if n==4:
        cloud_task('lab04-provision','Authorize and provision the Lab 04 healthy stack',core,
                   'Use the reviewed adapted Lab 4 template and healthy parameters. Record the exact stack plan and cost estimate, then deploy only after the learner authorizes the named resources. The learner performs the broken-deploy investigation; do not diagnose it for them.',
                   'Healthy stack exists in the approved account/region, is in the resource ledger, and its matching teardown row is LAB04 cleanup in this queue. The learner still owns milestone evidence.')
    add(f'LAB-{n:02}','Lab',f'Complete Lab {n:02}: {d["title"]}',d['objective'],core,d['deliverable'],
        'Complete all three handout milestones and preserve the required evidence/order. Explain them without an agent; keep interpretation and design choices your own.',
        supplement=starter,notes=d['boundaries']+' '+d['review']+(' The initial healthy stack was created by the preceding supervised provisioning prompt; inspect/explain it rather than blindly creating the same stack again. Later recreations remain part of the lab and need exact-resource destructive approval.' if n==4 else ''))
    if n==1:
        jit('lab01-transcript-export','Verify the Lab 01 transcript export path','Retain a complete, honest supervision record before using the tool for assignments.',source('policies.md'),
            '`labs/lab01/LOCATION.md`; the actual Lab 1 session; starter export script; chosen tool/model and the learner’s local transcript location under E:\\Codex when applicable.',
            ['Export one real session including prompts, assistant responses, tool calls/actions and ordering into the local lab transcripts/ directory. Adapt only the exporter if the chosen tool differs from the supported one.',
             'Open the export and compare a known tool action and result with the original session. Verify git ignore excludes transcripts/ and inspect git status so no lab transcript is staged.',
             'Record tool/model and a redacted local evidence path; do not fabricate missing transcript content or upload it to a public fork.'],
            '`labs/lab01/transcript-export-check.md` plus private local raw export; no transcript committed or pushed',
            'A real complete export is readable and checked against a tool action; lab transcripts are untracked and ignored.',kind='JIT verification')
    if n==8:
        jit('lab08-refuter','Run the Lab 08 fresh-context refuter and settle a finding',d['objective'],core,
            '`labs/lab08/LOCATION.md`; learner PLAN.md task scope; CHANGE-REQUEST.md; the single task diff including new files; closing clean-build evidence. Do not give the refuter the writer’s explanation.',
            ['Create a new session containing only the request, task scope and full task diff. Use a read-only brief asking for counterexample inputs/call sequences; any probe edits must stay temporary and within declared boundaries.',
             'Have the learner check the strongest finding using a new failing test or a concrete run/requirement citation. A false finding or no finding is a valid result if examined honestly.',
             'Record the brief, claim, reproduction or dismissal evidence, limits and learner verdict. Remove only named temporary probes; preserve relevant red-run evidence and leave shipped tests untouched.'],
            '`labs/lab08/refuter-review.md` linked from PLAN.md; settled finding and preserved evidence',
            'Fresh context is documented, at least the strongest claim has independent evidence, and temporary probe files are accounted for.',kind='JIT evaluation')
    if n==4:
        cleanup_lab(n,core)
    jit(f'{unit}-review',f'Review Lab {n:02} milestones independently',d['objective'],core,
        common_inputs+f' Learner deliverables: {d["deliverable"]}; final commit/diff and actual run evidence.',
        [f'Read the three milestones and learner evidence at the supplied commit. Review focus: {d["review"]}',
         'Run the smallest independent reproduction or inspect the relevant code trace; distinguish learner claims, actual results and remaining uncertainty. Respect handout rules on unchanged tests and staged patches.',
         f'Ask the learner, without an agent supplying answers, to explain one consequential decision and one limitation. Do not complete missing milestones for them. Record findings with severity and a concrete recheck.'],
        f'`reviews/{unit}-review.md` with three-milestone matrix, reproducible evidence, oral/self-recorded response and findings',
        'All three milestones have checked evidence and the learner can explain them; unresolved findings are recorded for the following correction row.',kind='JIT evaluation')
    if n in (8,9):
        cleanup_lab(n,core)
    add(f'LAB-{n:02}-CLOSE','Review',f'Address Lab {n:02} findings and record completion',d['objective'],core,
        f'`labs/{unit}/completion.md` and resolved review evidence',
        'Resolve required findings, rerun their focused checks, record the unassisted explanation, tool/model and final commit. Mark the lab complete only when its review and any required cleanup pass.',notes='Learner correction task; do not ask the assistant to solve the exercise wholesale.')


def cleanup_lab(n,core):
    text = {4:('Delete the approved Lab 4 stacks and any adaptation-only IAM/network resources, after saving DEPLOYMENT.md evidence. Cover each healthy/broken recreation. Verify terminated instances and no chargeable retained volumes/addresses/logs; Academy End Lab is not a personal-account teardown.',True),
            8:('Use the starter’s documented unlock mechanism for the exact modules locked for this lab; record restored access and remove only named refuter probes. Keep source, commits, plan and evidence.',False),
            9:('Capture load logs and X-Upstream evidence, inspect the exact Compose project, and stop/remove only its temporary containers/network. Obtain explicit approval before deleting any data volumes; retain baseline source, scripts and evidence.',False)}[n]
    jit(f'lab{n:02}-cleanup',f'Clean up Lab {n:02} temporary resources','Close the unit with evidence preserved and temporary resources accounted for.',core,
        f'`labs/lab{n:02}/LOCATION.md`; setup/deployment ledger and exact temporary resource inventory; learner evidence.',
        [text[0],'Record each resource before/after state and distinguish no residual billable resources from unverified or deliberately retained items. If a resource is retained, create a named dated-or-triggered teardown task in the queue and state its cost exposure.'],
        f'`labs/lab{n:02}/cleanup.md` and resource-ledger updates',
        'The named temporary resources are removed/unlocked with proof, or a learner-approved retained resource has a visible linked teardown task and explicit cost exposure.',kind='JIT cleanup',cloud=text[1])


def cloud_task(key,title,core,instruction,done):
    return jit(key,title,'Use the learner’s personal AWS account with verifiable identity, bounded costs and linked teardown.',core,
        '`progress/cloud-resources.md`; the current unit LOCATION.md and reviewed infrastructure diff; learner-selected profile and region names; prior AWS pre-check evidence. Do not read credentials files.',
        [instruction,'Apply the account/region/cost/approval controls below and update the per-resource ledger. Record actual resource IDs and whether the service is merely created or functionally healthy.'],
        'Unit-specific cloud evidence under reviews/ and updated `progress/cloud-resources.md` including matching teardown row',done,cloud=True,
        supplement=EXTERNAL['awsssm'][1])


def refresh(key,title,fallback):
    jit(f'{key}-refresh',f'Refresh missing source: {title}','Distinguish newly published CMU material from a labeled reconstruction before this unit.',SITE,
        '`curriculum/source-manifest.json`, source-and-gap-register.md, pinned Fall README and the current live Fall schedule/repository. Existing learner progress and any frozen contracts.',
        [f'Recheck the official Fall schedule and repository for {title}; save any newly available public handout/PDF and its SHA/date without overwriting the pinned snapshot.',
         'If official materials now exist, analyze them and update this unit’s resources, prerequisites, prompt specifics and coverage evidence. Keep current row IDs and preserve already released requirements.',
         fallback,
         'Record the source/fallback choice and any delta from the planning snapshot. Freeze this unit’s learner-facing handout and verification bar before its preparation or implementation.'],
        f'`reviews/{key}-source-refresh.md`, updated source register and versioned handout/resource pointer',
        'The unit has a verified official source or explicitly labeled, source-traceable reconstruction; no unavailable material is presented as recovered CMU content.',kind='JIT source review')


def hw_prepare(n):
    d=HWS[n]; core=source(f'assignments/hw{n}.md'); unit=f'hw{n:02}'
    jit(f'{unit}-release',f'Prepare and freeze Assignment {n:02}: {d["title"]}',
        f'Preserve the published Assignment {n} learning and acceptance obligations before learner implementation.',core,
        f'Inputs: {d["input"]}. Missing or private resources: {d["missing"]}. Read `assignments/{unit}/LOCATION.md` and assignment-continuity.md. Do not read future assignment releases.',
        [f'Read the entire official hw{n}.md and current-unit audit; obtain legally accessible original inputs if present and record revisions. Do not request access to CMU private repositories or imply that public substitutes recover them.',
         d['prep'],d['contract'],
         f'Write a requirement-to-source/verification matrix and `assignments/{unit}/release-manifest.json` containing version, SHA256 of the handout/requirements/rubric/input artifacts, status FROZEN, and the baseline repository commit. Record every reconstructed decision and compatibility obligation. Create learner-facing contract files in the recorded work repository, never in future units.',
         'Keep evaluator internals and any intentional-defect registry under assessments/withheld/ in an assessor-controlled session/repository; provide only criteria and bug-report-style findings to the learner. Do not write student specifications, designs, tests or solution code.'],
        f'`assignments/{unit}/release-manifest.json`, `assignments/{unit}/requirements.md`, current-unit `acceptance.md`, source mapping, private scaffold path and preparation evidence',
        f'Assignment {n:02} has versioned, complete and frozen current requirements/acceptance with provenance, all necessary inputs or labeled substitutes, and no learner implementation has begun.')
    jit(f'{unit}-assessor',f'Prepare independent Assignment {n:02} assessment controls',
        'Keep acceptance checks independent of the submitted implementation and evaluate the learner’s verification work.',core,
        f'Frozen `assignments/{unit}/release-manifest.json`, requirements.md and acceptance.md; `assessments/rubrics/{unit}.md`; current public brief. Assessor session only, separate from learner work.',
        [f'Create only current-unit assessor fixtures/checks under `assessments/withheld/{unit}/`. Derive each check from a frozen requirement or published behavior-preservation obligation, not from the eventual solution. Record the mapping and hashes before inspecting learner implementation.',
         d['acceptance'],
         'Where the learner harness/characterization tests are assessed, create minimal correct and incorrect controls that distinguish checking behavior from pinning implementation. Validate control verdicts independently; a control is not a learner reference solution. Keep controls and expected failures out of prompts, notes and learner-visible logs.',
         'Expose only an assessment interface/run command and output format in current acceptance.md; do not expose private expected values or mutation details. If the same learner controls both roles, record that filesystem separation prevents accidental spoilers but cannot provide genuine hidden-grader independence.'],
        f'Private `assessments/withheld/{unit}/` evaluator and control-validation log; public invocation/criteria in `assignments/{unit}/acceptance.md`',
        'Every independent check maps to frozen obligations, assessor controls have demonstrated expected verdicts, and no student solution was used to define acceptance.',kind='JIT evaluation setup')
    jit(f'{unit}-preflight',f'Verify Assignment {n:02} inputs and starter',
        'Separate runnability from the functionality the learner is meant to implement.',core,
        f'`assignments/{unit}/LOCATION.md`, frozen release manifest, current scaffold, prior application commit where applicable and preparation evidence. {d["input"]}',
        [f'Verify manifest hashes and required files for Assignment {n:02}. Run only the current starter’s documented build/start/health checks. For HW4, use the exact-tag quick build, core suite and specified functional slice from the brief; for HW5 validate scaffold/replica reachability without repairing correctness; for HW6 verify inputs/config locally without provisioning yet.',
         'Record expected versus observed starter tests, including intended failures or missing future functionality. Verify the chosen tool’s complete private transcript export and current repository privacy without creating a new public remote.',
         'Confirm previous contracts/client/ADRs are preserved for HW3/5/6 and the HW4 subsystem boundary is enforced. If requirements or scaffold are incomplete, block implementation and save a specific recovery task.'],
        f'`assignments/{unit}/preflight.md` with file/hash, runnability, transcript and continuity evidence',
        'Current inputs exist, frozen hashes match, the starter runs as documented and intentional deficiencies remain; any billable action waits for its cloud row.',kind='JIT verification')
    if n==1:
        add('HW-01-AUDIT','Assignment','Assignment 01 Phase 1: understand and audit',
            'Interpret claims and distinguish suspicious code from an evidenced defect.',core,'AUDIT.md claim interpretations, checks and severity judgments',
            d['checkpoint'],notes='May begin after the initial agent-workflow lectures. Repairs/testing wait for the testing lectures and Lab 2.')


def checkpoint(n):
    d=HWS[n];core=source(f'assignments/hw{n}.md');unit=f'hw{n:02}'
    if n==6:
        cloud_task('hw06-checkpoint-deploy','Provision Assignment 06 checkpoint deployment',core,
                   'Use the current frozen deploy/ baseline in the progressive app. Present a minimal personal-AWS plan, authorize it, then deploy. The learner owns pipeline and observability implementation. Link this deployment to the checkpoint-teardown row immediately following checkpoint review.',
                   'Approved stack runs and is inventoried with a matching checkpoint teardown; do not mark the learner checkpoint complete without its own pipeline and ADR evidence.')
    add(f'HW-{n:02}-CHECKPOINT','Assignment',f'Complete Assignment {n:02} checkpoint: {d["title"]}',
        'Make design and verification commitments before completing implementation.',core,d['checkpoint'],
        'Commit the complete checkpoint artifacts and record the immutable commit; preserve the brief’s order and word/scope limits.',
        notes='Original checkpoint intent; calendar deadlines replaced by dependency order. Freeze learner-owned capability/policy commitments before main implementation.')
    jit(f'{unit}-checkpoint-review',f'Review Assignment {n:02} checkpoint and freeze learner specifications',
        'Verify the checkpoint is meaningful and its learner-chosen acceptance obligations are fixed before main implementation.',core,
        f'Checkpoint commit for {unit}; release-manifest.json; public brief; {d["checkpoint"]}',
        [f'Check this exact checkpoint against the brief: {d["checkpoint"]}',
         'Have the learner resolve only ambiguity that prevents objective verification, without prescribing a design or solution. Freeze current CAPABILITY.md/NOTIFICATIONS.md/observability commitments where applicable and hash the accepted checkpoint. Preserve historical checkpoint text where the brief requires it.',
         'Do not retroactively relax released core/acceptance requirements. If a learner-owned specification must change later, append a reviewed version/ADR and retain the earlier compatibility contract; document the adaptation from the official brief’s revision allowance.',
         'Record complete or required findings with a concrete recheck. The next correction gate must clear before implementation proceeds.'],
        f'`reviews/{unit}-checkpoint.md`, frozen checkpoint commit/hashes and specific findings',
        'Checkpoint artifacts are independently inspected; frozen obligations, uncertainties and required corrections are recorded.',kind='JIT evaluation')
    add(f'HW-{n:02}-CHECKPOINT-CLOSE','Review',f'Resolve Assignment {n:02} checkpoint findings',
        'Enter implementation with an explicit, reviewable contract and verification plan.',core,
        f'accepted checkpoint commit and `assignments/{unit}/checkpoint-signoff.md`',
        'Required checkpoint findings pass their rechecks; the current released contract and learner specification hashes are recorded before main implementation.')
    if n==6:
        cloud_task('hw06-checkpoint-teardown','Tear down idle Assignment 06 checkpoint infrastructure',core,
                   'Capture health, pipeline and checkpoint telemetry first; inspect the exact ledger inventory, obtain destructive-action approval and remove idle checkpoint resources. Keep images/configuration needed for a later fresh deployment. The operating-block provisioning row recreates only what is needed.',
                   'Checkpoint evidence survives and no unapproved billable checkpoint resources remain; retained artifacts and charges are explicitly inventoried.')


def hw_finish(n):
    d=HWS[n];core=source(f'assignments/hw{n}.md');unit=f'hw{n:02}'
    add(f'HW-{n:02}-BUILD','Assignment',f'Complete Assignment {n:02}: {d["title"]}',
        'Implement under frozen requirements with validation-first supervision and honest engineering memory.',core,d['final'],
        'Deliver every required artifact at an immutable commit with actual verification evidence. Follow frozen requirements, not an assistant’s changing interpretation.',
        notes=f'{d["final"]} Assessment: {d["acceptance"]}')
    if n==2:
        cloud_task('hw02-deploy','Demonstrate Assignment 02 AWS deployability',core,
                   'Inspect the learner’s README/IaC, estimate and authorize a bounded deployment, then follow the README from a clean context. Capture server/frontend health as appropriate without changing implementation or the frozen API. Link every resource to the next teardown row.',
                   'README deployment steps are independently demonstrated on AWS, or a concrete deployment finding blocks acceptance; all resources are inventoried.')
        cloud_task('hw02-teardown','Tear down the Assignment 02 deployment',core,
                   'Save deployment demonstration evidence, present exact resource IDs for approval, then delete only the authorized demo stack and temporary supporting resources. Check residual EBS/IPv4/log/storage charges.',
                   'Deployment evidence is saved and all demo billable resources are removed or explicitly retained with an approved visible teardown task.')
    jit(f'{unit}-acceptance',f'Evaluate Assignment {n:02} against the frozen contract',
        'Judge functionality, verification quality, design, memory and supervision using independent evidence.',core,
        f'Final learner commit and repository path from `assignments/{unit}/LOCATION.md`; frozen release and checkpoint manifests; `assessments/rubrics/{unit}.md`; private assessor run interface. Expected deliverables: {d["final"]}',
        ['Verify frozen requirement and evaluator hashes before running. Use a clean workspace and redact secrets. Compare the final commit with its declared baseline; never modify the submission to make checks pass.',
         d['acceptance'],
         f'Apply the published rubric dimensions and report independent evidence per item: {d["weights"]}. Preserve the distinction between a verified pass, fail, blocked input, and unassessed item. Original hidden-grader points receive reconstructed evidence, never a claim of official equivalence.',
         'Inspect plans/transcripts/ADRs against commit history. Challenge one design assumption and one claimed testing boundary. Report reproducible behavior/requirement findings without dumping withheld tests or worked fixes.',
         'Save findings and focused rechecks for the learner; do not implement corrections. Cloud activities in this unit must show executed cleanup or a visible learner-approved retention/teardown task.'],
        f'`reviews/{unit}-acceptance.md`, per-requirement results, rubric evidence, limits and findings at the assessed commit',
        'Every frozen obligation has an evidenced result or explicit unresolved finding; no claim relies solely on AI review or an unrecovered CMU grader.',kind='JIT evaluation')
    if d['defense']:
        jit(f'{unit}-defense',f'Conduct Assignment {n:02} unassisted defense',
            'Defend real decisions and demonstrate ownership of the submitted system.',core,
            f'Final assessed {unit} commit, learner notes and the public defense questions in hw{n}.md. No worked answer or live coding-agent assistance.',
            [f'Choose one public hw{n} defense question and a follow-up counterfactual. Give the question, then stop for the learner’s own spoken or recorded answer; do not answer it for them.',
             'Record the question, learner evidence and whether the answer is consistent with the code and records. HW4 requires a correct subsystem walkthrough; HW1/2/3/5 use the brief’s completeness-oriented conversation bar.',
             'For self-study without a human examiner, save an unassisted voice/text answer first and critically compare it afterward; identify this limitation explicitly and never claim official TA signoff.'],
            f'`reviews/{unit}-defense.md` with actual learner response evidence and follow-up',
            'The learner supplied an unassisted response about actual work and the review records its accuracy/completeness and limits; a pending response stays Blocked.',kind='JIT defense')
    cleanup_focus={
        1:'Stop only the identified Bad Slack backend/frontend and test-harness processes. Preserve the assessed database snapshot if needed for evidence; leave server/data.sqlite* uncommitted. Do not identify processes solely by a reused port.',
        2:'Stop only current local application/frontend/harness processes after all checks. Preserve the progressive application database/volumes, frozen v1, capability contract, harness and founding decisions for HW3.',
        3:'Stop temporary v1-client probes and old/regenerated test instances after saving verdicts. Preserve the accepted same-application data, old contracts/client, harness, frontend and decision history for HW5.',
        4:'Stop only the Jetty/Jenkins processes and temporary test instances started for this assignment. Preserve the exact-tag full-history working tree, proposal, new tests and evidence; do not clean or rewrite upstream history.',
        5:'Capture the 1/2/4 replica and notifier evidence, then stop the exact local Compose project and assessor simulator. Preserve named data volumes, accepted v3 configuration and service records for HW6. Do not delete volumes without exact-inventory approval.',
        6:'Check the completed cloud teardown/capture rows first; stop remaining identified local stand-ins and traffic probes. Retain private learner telemetry and independent assessor archives. Account for retained registry/log/storage charges explicitly.'
    }[n]
    jit(f'{unit}-local-cleanup',f'Close Assignment {n:02} local processes and preserve its evidence',
        'Finish the unit without losing continuity or leaving unmanaged temporary processes.',core,
        f'`assignments/{unit}/LOCATION.md`, assessed commit/review, actual process/Compose inventories and unit-specific run logs. {d["final"]}',
        [cleanup_focus,
         'Identify ownership from the recorded working directory, command line or Compose project before stopping anything. Remove only explicitly identified disposable probes; preserve source, data and assessed evidence. Obtain explicit approval for destructive repository/data operations.',
         'Record process/resource after-state, preserved artifacts and the next-unit input commit. This local cleanup does not replace any cloud teardown row.'],
        f'`assignments/{unit}/cleanup.md` with identified processes stopped and continuity/evidence preservation',
        'Only current-unit temporary processes/probes are closed, assessed evidence and required application state survive, and any billable resources are handled by their linked cloud teardown.',kind='JIT cleanup')
    add(f'HW-{n:02}-CLOSE','Review',f'Resolve Assignment {n:02} findings and archive the baseline',
        'Carry forward a verified application baseline and explicit uncertainty.',core,
        f'`assignments/{unit}/completion.md`, accepted commit, preserved contract/ADRs/reviews and next-unit input pointer',
        'Required findings pass focused rechecks; review/defense evidence is saved where required, private transcripts exist, cloud cleanup is accounted for and completion cites an immutable commit.',
        notes='Do not silently change frozen acceptance. Append new ADRs for changed choices and keep previous contract files available for future compatibility checks.')


def exam(name,title,scope,minutes,core):
    jit(f'{name}-prepare',f'Prepare reconstructed {title} self-assessment',
        'Assess independent reasoning with unseen questions while distinguishing self-study from official CMU exams.',core,
        f'Completed notes and reviewed work in scope: {scope}. Public learning goals and any officially published practice questions available at this trigger. No private Canvas exam is presumed recovered.',
        [f'Create a reconstructed assessment blueprint for {scope}, using explanation, code reading, counterexample and tradeoff questions. Preserve {minutes} minutes as a suggested sitting length, not a calendar deadline.',
         'Save blank learner paper and rules separately from assessor-only questions/answers/rubric. Prefer an independent assessor to hold unseen questions; otherwise disclose the limitation. Include one check per major learning objective without giving model answers in the learner prompt.',
         'Freeze scope and scoring criteria before the learner sees the questions. For Midterm 1 exclude L08 as new content; for Midterm 2 focus L08–L16 and Jenkins, not L17 as new content. Final covers the full mapped course.'],
        f'`assessments/{name}/instructions.md`, frozen blueprint and assessor-only paper/key under withheld/',
        'A labeled reconstructed assessment has frozen scope/criteria and no learner-visible answer key.',kind='JIT assessment setup')
    add(name.upper(),'Evaluation',f'Sit the reconstructed {title} unassisted','Demonstrate course reasoning independently.',core,
        f'`assessments/{name}/learner-response` and time/rules record',
        'Attempt the frozen paper without any agent, then preserve the original answer before review.',notes=f'Scope: {scope}. Original exam paper unavailable; reconstruction is not official grading. Suggested duration: {minutes} minutes.')
    jit(f'{name}-review',f'Review {title} evidence and plan targeted remediation','Use independent reasoning gaps to guide further study.',core,
        f'Frozen {name} blueprint/key, immutable unassisted learner response, source-cited scope and notes.',
        ['Assess against the frozen rubric only after the response is saved. Check reasoning, not fluent phrasing; record counterexamples and misunderstood assumptions.',
         'For every material gap assign a specific existing reading page or bounded recall exercise and a verification question. Save a task-specific remediation prompt if agent-guided operational work is needed; do not insert generic busywork.',
         'Keep original responses/scores immutable; record a separate corrected explanation and recheck before the following closure row completes.'],
        f'`reviews/{name}.md`, source-specific remediation and a recheck result',
        'Every assessed objective has evidence and material gaps have concrete rechecks; assessment remains labeled reconstructed.',kind='JIT evaluation')
    add(name.upper()+'-CLOSE','Review',f'Resolve {title} reasoning gaps','Close demonstrated prerequisite gaps before advancing.',core,
        f'`assessments/{name}/corrections.md`','Required remediation questions are answered unassisted and checked; unresolved gaps have explicit blocked recovery rows.')


def make_queue():
    jit('prerequisites','Check self-study prerequisites and progress conventions',
        'Confirm programming/invariant readiness and initialize an executable self-paced queue.',source('learninggoals.md'),
        'The workbook, root AGENTS.md, public course overview/policies, existing Spring tracker in the preserved sibling directory, and a learner explanation of a small program and invariant. No cloud credentials needed.',
        ['Inspect the existing learner workspace without changing the Spring course. Ask the learner to explain a loop/invariant and a basic collection operation; record actual evidence rather than assume two programming courses.',
         'If Java interfaces or TypeScript/HTTP vocabulary is unfamiliar, use the immediately queued conditional prerequisite readings and record the gap. Install only tools due for Lab 1/HW1 later; no blanket environment provisioning.',
         'Explain workbook status/evidence handling, personal ownership of specs/decisions, private assignment transcripts versus local-only lab transcripts, frozen requirements and how to recover a blocked row. Confirm chosen tool export during Lab 1, not from old setup memories.',
         'Record any missing baseline skill as a named recovery activity and its specific check before dependent work.'],
        '`progress/prerequisites.md` with learner readiness evidence, gaps and next row ID',
        'Readiness is evidenced or blocked with a named recovery task; the next workbook row is unambiguous.')
    lecture(1)
    lecture(2)
    supplement('SUP-JAVA','Check Java interfaces and object vocabulary if unfamiliar','Read Java code used in Lab 1 without relying on agent paraphrases.',EXTERNAL['java'][1],
               'Explain visibility, object identity, an interface and constructor injection using a short non-exercise example; if already proficient record the evidence and waiver.','Conditional prerequisite, not an extra programming assignment.')
    supplement('SUP-HTTP','Learn request/response and HTTP status vocabulary','Read the public HW1 health/signup obligations.',EXTERNAL['http'][1],
               'Explain a request method/path/body and 200, 201, 400, 401, 404, 409 responses; record known versus newly learned concepts.')
    lab(1)
    hw_prepare(1)
    lecture(3)
    supplement('SUP-DOUBLES','Clarify test doubles if needed','Distinguish a fake, stub and mock and their oracle limits.',SPRING+'labs/lab07.md',
               'Use the Spring definitions only; explain one double and its drift risk, or record an evidenced waiver. Do not execute the Spring lab.')
    lecture(4)
    supplement('SUP-JQWIK','Read jqwik property and shrinking mechanics','Use generated inputs and interpret a minimal counterexample in Lab 2.',EXTERNAL['jqwik'][1],
               'Explain property annotation, generator constraints, seed/reproduction and shrinking without writing the Lab 2 property.')
    lab(2)
    supplement('SUP-FASTCHECK','Read fast-check core blocks','Translate property concepts to the HW1 TypeScript harness.',EXTERNAL['fastcheck'][1],
               'Explain arbitrary, property and assert with reproducible seed/path output; do not fill the assignment property scaffold.')
    hw_finish(1)
    lecture(5)
    hw_prepare(2)
    lab(3)
    cloud_task('aws-personal-readiness','Check personal AWS readiness before Lab 04',source('labs/lab03.md'),
               'Replace the Lab 3 Academy invitation/green-dot step with a personal-account check. Verify existing CLI v2 and secure sign-in, account/role/profile/region, SSM permissions, default VPC/subnet availability and a learner-approved cost envelope. Identify Lab 4 template hard-coded profile/key and ingress assumptions. Record needed IAM/network adaptations without deploying any billable resource.',
               'The learner’s intended account/profile/region and necessary permissions/network adaptations are recorded safely, current estimated cost exposure is understood, and no billable stack was created.')
    lecture(6)
    checkpoint(2)
    lecture(7)
    lab(4)
    hw_finish(2)
    lecture(8)
    exam('exam1','Midterm 1','L01–L07, HW1/HW2 and Labs 1–4; exclude L08 as new material',80,source('slides/08-modularity-and-anti-patterns.pdf')+'#page=60')
    hw_prepare(3)
    lab(5)
    lecture(9)
    supplement('SUP-COMPOSITION','Review inheritance versus delegation if needed','Read polymorphic designs and compare their coupling.',SPRING_DECKS['Inheritance and Delegation'],
               'Explain one composition/inheritance tradeoff and what overriding does, or record an evidenced waiver.')
    lecture(10)
    checkpoint(3)
    supplement('SUP-LAB06-API','Read the Lab 06 early API evolution primer','Predict additive/breaking changes before the main API lecture.',source('labs/lab06.md')+'#some-concepts-that-will-be-helpful',
               'Define additive, breaking and deprecation using a non-lab API; leave milestone predictions to the learner.')
    lab(6)
    lecture(11)
    hw_finish(3)
    lecture(12)
    hw_prepare(4)
    lab(7)
    lecture(13)
    supplement('SUP-MCP','Inspect the MCP host/client/server boundary','Distinguish a tool protocol from agent policy and orchestration.',EXTERNAL['mcp'][1],
               'Sketch participants and one tool request; state that MCP does not determine model judgment or application permission policy. No server installation required.')
    lecture(14)
    checkpoint(4)
    lab(8)
    lecture(15)
    hw_finish(4)
    lecture(16)
    supplement('SUP-COMPOSE','Read Compose scaling and k6 thresholds','Understand replica reachability and a failing load-test verdict before Lab 9/HW5.',EXTERNAL['compose'][1],
               'Explain --scale, service DNS and the --no-deps load-run precaution; read the linked k6 threshold reference from Resources and describe one metric threshold without writing lab scripts.')
    hw_prepare(5)
    lab(9)
    lecture(17)
    exam('exam2','Midterm 2','L08–L16 and Jenkins/XML persistence, with earlier design reasoning assumed; exclude L17 as new material',80,source('slides/16-data-models-at-scale.pdf')+'#page=2')
    lab(10)
    checkpoint(5)
    lecture(18)
    lecture(19)
    lab(11)
    hw_finish(5)
    lecture(20)
    hw_prepare(6)
    lecture(21)
    supplement('SUP-PYTHON','Review Python environment and annotation basics if needed','Run the Lab 12 toolchain while preserving its deliberate gate discoveries.',EXTERNAL['venv'][1],
               'Explain isolated interpreter/pip/pytest paths and a function annotation; do not run or fix Lab 12 static checks before milestone 2.')
    lab(12)
    refresh('lec22','Supply Chain Security lecture','If no Fall PDF is available, use the exact Spring Supply Chain Security deck where accessible; supplement its remaining build-provenance gap with SLSA threats, and save a reconstructed study brief without inventing Fall slide content.')
    add('LEC-22','Lecture','Supply Chain Security — source refresh or reconstructed study',
        'Review dependency/build/credential trust boundaries and select evidence for supply-chain gates.',SITE+'#schedule',
        'notes/LEC-22.md and a source-cited dependency/action/image trust map',
        'Use the refreshed Fall deck if published; otherwise complete the labeled Spring/SLSA study guide and explain a provenance guarantee and its limit.',
        supplement=SPRING_DECKS['Supply Chain Security'],notes='No linked Fall PDF in pinned snapshot; reconstructed fallback described in curriculum/reconstructed-study-guides.md.')
    checkpoint(6)
    refresh('lec23','Observability and Monitoring lecture','If still unlinked, use the HW6 observability obligations plus Google SRE Ch.6 and OpenTelemetry signal definitions; save a reconstructed study brief and identify which choices remain the learner’s.')
    add('LEC-23','Lecture','Observability and Monitoring — source refresh or reconstructed study',
        'Correlate request logs, meaningful metrics and user-visible alerts; separate a symptom from fault localization.',SITE+'#schedule',
        'notes/LEC-23.md: signal map, user-visible alert rationale and telemetry-only request trace plan',
        'Complete the refreshed Fall material or labeled SRE/OpenTelemetry guide; explain latency/error/silent-failure visibility without implementing HW6 instrumentation for the learner.',
        supplement=EXTERNAL['sre'][1],notes='No linked Fall PDF in snapshot; fallback is reconstructed, not an official lecture.')
    add('HW-06-INSTRUMENT','Assignment','Complete the Assignment 06 pipeline, telemetry and degradation plan',
        'Make the running system and its deployment independently observable and verifiable before operation.',source('assignments/hw6.md'),
        'Full gated CI/CD, static/audit/gitleaks checks, safe failure probes, commit-reporting health, structured logs, meaningful metric, demonstrated alert and three contemporaneous ADRs',
        'Implement all pipeline and observability obligations in the frozen HW6 brief; demonstrate blocking synthetic nonsecret/security controls safely, exercise an alert with an announced local stand-in, and commit the degradation plan before the real operating block.',
        notes='Learner implementation task. Do not use live secrets or real vulnerable deployments as probes. Tests/static/audit/secret jobs, branch/time/caching/concurrency rules, private images and exact-commit health wait must be verified before operation.')
    jit('hw06-operation-preflight','Verify Assignment 06 operating readiness before deployment',
        'Require objective pipeline and telemetry evidence before beginning the billable operating block.',source('assignments/hw6.md'),
        'HW-06-INSTRUMENT commit, frozen HW6 requirements/acceptance, local health/alert evidence, CI history, source/image secret-scan and rotation evidence if applicable, private deploy configuration names and the cloud ledger.',
        ['Inspect the learner pipeline at the proposed commit and actual runs. Verify tests, chosen static gate, dependency audit and gitleaks 8.30.1, a whole-history scan at least once, then correct new-commit scan coverage, and a safely synthetic non-live-secret rejection proof. Judge the critical-vulnerability gate using an isolated controlled fixture, never a live vulnerable service.',
         'Verify branch rules, separate checks, job timeouts, cancellation of obsolete runs, dependency cache, documentation-only skip, main-only deployment and private image publication. Confirm the final deploy step waits for the health x_ field to equal the built commit and has a bounded timeout.',
         'Inspect structured log correlation/user/message/status fields, metric behavior and a demonstrated user-visible alert. Check the degradation ADR is committed before the operating block, no keyed URL leaks into logs/images/config commits, and the request trace can be followed without code.',
         'Record gaps for learner correction. Do not start or authorize the operating block until the required pre-operation checks pass; environment/service provisioning remains in the following explicit rows.'],
        '`assignments/hw06/operating-preflight.md` and immutable pipeline/alert/security evidence',
        'The full pipeline, safe blocking probes, local instrumentation/alert and pre-operation records have independent evidence; every required gap is resolved before deployment.',kind='JIT verification')
    jit('hw06-operating-service','Prepare the independent HW06 operating-block service and freeze its interface',
        'Make operation independently executable without exposing a planned failure or rewriting v3 obligations.',source('assignments/hw6.md'),
        'HW6 frozen requirements and current learner stack; original course operations/ service if lawfully accessible; otherwise the current-unit reconstructed service specification; separate assessor repository/account and private NOTIFY_URL configuration.',
        ['Assessor only: prepare a separate reachable service matching the frozen notify/ack interface, a retained timestamped service-side record and at least one latency/error/silent-delivery degradation during a ≥3.5-hour block. Save the schedule and reference record only under withheld/. A physically separate host/process with retained records is preferred; disclose learner-controlled assessor limitations.',
         'Validate healthy interface and a private fault-mode control before the learner block; keep timing unknown to the learner, while exposing the allowed observation endpoints and acknowledgment protocol. Use no live credential in a test fixture or chat.',
         'Freeze the synthetic traffic generator before the block. Obtain the learner’s chosen start trigger and duration without imposing semester dates. Prepare current-unit service run and capture instructions; link all service-side billable resources to the operating teardown row.'],
        'Private assessor service/runbook/fault record; public frozen operations interface and traffic hash; cost/teardown ledger if billable',
        'A healthy and privately fault-tested assessor service is reachable, records independent evidence, keeps fault timing withheld and has a linked teardown; the learner can run the block from saved instructions.',kind='JIT service preparation',cloud=True)
    cloud_task('hw06-operating-deploy','Provision the Assignment 06 operating block',source('assignments/hw6.md'),
               'Review and authorize the final minimal AWS stack and monitoring costs, then deploy only through the learner’s gated main pipeline. Require the health response to report the exact built commit; verify frozen traffic and secret-free configuration before beginning the block. Match both learner and assessor resources to the operating-teardown row.',
               'The approved deployed commit passed its full pipeline, health reports that commit, frozen traffic reaches the independent notifier, and telemetry/alert/service records are ready before starting the block.')
    add('HW-06-OPERATE','Assignment','Operate Assignment 06 for a continuous block of at least 3.5 hours',
        'Observe a real deployed system under a service degradation without compromising core correctness.',source('assignments/hw6.md'),
        'operating-block start/end, immutable traffic hash and running commits, actual telemetry, evidence-based acknowledgment and independent service record',
        'Operate at least 3.5 continuous hours with frozen traffic and monitoring. Record actual observations and one degradation acknowledgment supported by telemetry; preserve v1–v3 behavior during failure.',
        notes='Self-paced adaptation of the fixed December block. Duration is preserved; original calendar dates are not imposed. Do not simulate elapsed runtime or fabricate logs.')
    jit('hw06-capture','Capture Assignment 06 telemetry before teardown','Preserve evidence needed for independent incident analysis.',source('assignments/hw6.md'),
        'Operating-block resource inventory, start/end and deployed commits; learner logs/metrics/alerts; separately retained assessor service record; private secret configuration.',
        ['Copy raw learner telemetry to the private application telemetry/ directory, preserving timestamps, event/message IDs and commit identity. Verify copies are readable and span the entire operating block before removing resources.',
         'Scan logs for NOTIFY_URL/key leakage without printing secrets. If exposed, rotate and record redacted revocation proof; retain engineering evidence with only permitted privacy redactions.',
         'Assessor separately retains the service-side record and fault history; provide only the public observations authorized by the frozen interface until incident submission is saved. Hash both evidence archives.'],
        'Private learner telemetry/ archive, independent assessor archive and checksum manifest',
        'Readable complete learner telemetry and independent service evidence are safely copied and hashed before any resource deletion.',kind='JIT evidence capture')
    cloud_task('hw06-operating-teardown','Tear down the Assignment 06 operating block',source('assignments/hw6.md'),
               'Verify telemetry-copy hashes, then present the exact learner and assessor resource inventories for destructive approval. Stop frozen traffic and delete only approved temporary stacks/resources. Verify absence of retained billable infrastructure; keep private images only if explicitly retained with storage cost and a linked cleanup task.',
               'Traffic has stopped, evidence survives, and learner/assessor cloud inventories show no unapproved residual charges or an explicitly approved visible retention/teardown task.')
    refresh('lec24','Summary and What We Learned Together lecture','If still unlinked, reconstruct a synthesis using the official learning goals and the learner’s six evidence records. Ask for revised decisions and uncertainty, not a fictional official summary.')
    add('LEC-24','Lecture','Summary and What We Learned Together — source refresh or reconstructed synthesis',
        'Connect verification, change, reuse, scale, operations, supervision and engineering memory.',source('learninggoals.md'),
        'notes/LEC-24.md mapping each course goal to personal evidence and a remaining limitation',
        'Explain one decision that changed across HW2/3/5/6, one Jenkins lesson, and one unresolved weakness using actual artifacts.',notes='Official scheduled title; reconstructed synthesis if no Fall deck is available.')
    hw_finish(6)
    lab(13)
    exam('final','Final Exam','All mapped Fall learning goals, six assignments and labs, including HW6 operations reasoning',180,source('learninggoals.md'))
    jit('course-reconcile','Reconcile final course evidence and residual resources','Close the course with honest traceability and no stranded operational tasks.',source('learninggoals.md'),
        'The complete workbook, all unit completion/review records, cloud ledger, private assignment locations/transcripts and current source/gap register.',
        ['Reconcile every activity, linked prompt and immutable evidence artifact. Record unresolved goals/deviations; do not manufacture attendance, quizzes, oral defenses or CMU grading.',
         'Recheck current official material availability for future refreshes and preserve differences from frozen assignments. Confirm every billable resource is deleted or has explicit learner-approved retention and a visible teardown task.',
         'Record completion per goal and next deliberate study action; update the workbook without renumbering IDs. Keep withheld assessment material separated from the learner archive.'],
        '`reviews/course-reconciliation.md`, reconciled workbook, final private evidence index and resource-ledger verdict',
        'Each course goal maps to actual evidence or an explicit unresolved item, no unaccounted billable resources remain, and progress status matches the records.',kind='JIT review')


def documents():
    concept=['# Concept and prerequisite map','',
             'Reconstructed study map derived from every available Fall deck. The official Fall schedule determines the order; dates and breaks do not become learner deadlines. The deck filename defines the stable lecture ID even where slide title/footer numbering is inconsistent.','',
             'Each lecture row requires an unassisted recall answer in the learner’s own notes. These replace unavailable in-class participation activities for self-study; they are not official quizzes.','']
    reviews=['# Fall lecture review','',
             'Review basis: all 21 published PDF decks were extracted page by page and examined using page-indexed text digests, targeted full-text examples and selected rendered diagram/image slides. Complete text and PDFs are retained locally. This is a text-led instructional analysis, not an exhaustive visual review of every slide or access to recorded teaching. Sparse/image slides need the source visual; no unseen speech or Canvas material is inferred.','',
             'The [page index](lecture-page-index.md) records extraction coverage for every PDF page. [pdf-extraction.json](pdf-extraction.json) records counts and sparse pages. The following per-deck judgments distinguish supplied teaching from operational/prerequisite gaps.','']
    for n,d in enumerate(LECTURES,1):
        code,title,obj,pages,examples,pre,gap,spring,question=d
        url=source(f'slides/{code}.pdf')
        concept += [f'## LEC-{n:02}: {title}', '',f'- Objective: {obj}',f'- Source: [{code}.pdf]({url}); PDF pages {pages}.',f'- Prerequisites: {pre}',f'- Concepts/explanations/examples: {examples}',f'- Independent explanation check: {question}',f'- Gap action: {gap}',f'- Spring comparison: '+(f'[{spring}]({SPRING_DECKS[spring]}) — targeted support, not mandatory duplicate coursework.' if spring else 'No matching Spring replacement required; use Fall.'),'']
        reviews += [f'## LEC-{n:02}: {title}', '',f'Source: [{code}.pdf]({url}); focal pages {pages}.', '',f'**Supplied teaching and examples.** {examples}', '',f'**Assumed prerequisites.** {pre}', '',f'**Gap judgment.** {gap}', '',f'**Verification.** {question}', '']
    concept += ['## LEC-22–24 and Lab 13','',
                'The pinned Fall schedule names Supply Chain Security, Observability and Monitoring, Summary and What We Learned Together, and Lab 13 Make It Observable without linked Fall materials. Each has its own source-refresh task before study/setup. Use newly published official material when available, otherwise the labeled [reconstructed study guides](reconstructed-study-guides.md) and the Lab 13 release prompt. No fabricated Fall PDF is supplied.','',
                '## Dependency graph','',
                '```mermaid','flowchart LR','  Basics[Programming and invariants] --> Verify[L01–04: workflow and verification]',
                '  Verify --> Repair[HW1 isolated flawed app]','  Verify --> Design[L05–11: design and reuse]',
                '  Design --> V1[HW2 progressive app v1]','  V1 --> V2[HW3 same app v2]',
                '  Design --> Memory[L12–14: memory and supervision]','  Memory --> Jenkins[HW4 separate Jenkins XML subsystem]',
                '  V2 --> Scale[L15–19: architecture state concurrency coordination]',
                '  Scale --> V3[HW5 same app v3 replicas]',
                '  V3 --> Ops[L20–23 and HW6: same v3 system operated]',
                '  Jenkins --> Ops','  Ops --> Synthesis[L24 Lab13 and final assessment]','```','',
                'The Excel queue adds explicit preparation, preflight, checkpoint, assessment, correction and teardown gates to this conceptual graph. Prerequisite support is inserted where needed: Java before Lab 1, HTTP before HW1, property-library syntax before Lab 2/HW1, inheritance before patterns, early API primer before Lab 6, Compose/k6 before replicas, Python before Lab 12.']
    write('curriculum/concept-map.md','\n'.join(concept))
    write('curriculum/lecture-review.md','\n'.join(reviews))
    lab_lines=['# Public lab audit','',
               'Static audit only: complete Fall handouts and each public starter SETUP.md, manifests, CI configuration, named templates and staged-file presence were inspected. No lab runtime was installed, no starter tests were run and no defects were repaired during syllabus construction. Expected counts below are source claims, not observed passes. Exact source revisions and file hashes are in [source-manifest.json](source-manifest.json).','']
    for d in LABS:
        n=d['n'];name=f'lab{n:02}'; core=source(f'labs/{name}.md') if n<13 else SITE+'#schedule'
        lab_lines += [f'## Lab {n:02}: {d["title"]}','',f'Handout: [{name}]({core}). '+(f'[Original public starter](https://github.com/CMU-17-214/f26-{name}); archived at `course-materials/starters/f26-{name}/`.' if n<13 else 'Handout/starter unlinked in snapshot; release or reconstruction is deferred to its source-refresh row.'),
                      '',f'- Objective: {d["objective"]}',f'- Tools: {d["tools"]}',f'- Minimal JIT health command: `{d["check"]}`',f'- Expected starter state: {d["baseline"]}',f'- Required artifacts audited: {d["files"]}',f'- Adaptation and scope: {d["boundaries"]}',f'- Milestone evidence: {d["deliverable"]}',f'- Review focus: {d["review"]}','']
    lab_lines += ['## Material personal-account adaptation: Lab 4','',
                  'The actual `infra/template.yaml` sets `IamInstanceProfile: LabInstanceProfile`, `KeyName: vockey`, assumes usable default networking and opens SSH 22 to 0.0.0.0/0 in addition to the service port. Its comment claiming only service ingress does not match that SSH rule. The four-hour shutdown stops the instance but does not delete the stack/disks or guarantee zero charges.','',
                  'At the Lab 4 JIT trigger, parameterize/provide the personal-account instance profile with required SSM permissions; remove the Academy key requirement when SSM is sufficient, or use an explicitly selected private key without copying it into the repo. Restrict/remove SSH and inspect network availability; create an explicit minimal VPC/subnet only if needed. Review all IAM/network changes and cost estimates before execution. Keep scenario parameters intact and track the adaptation diff against the archived original. Do not build the adaptation now.','',
                  '## Other operational observations','',
                  '- Labs 8 and 9 are distinct pristine starter revisions (418+137 versus 478+150 tests). Lab 9 is not the learner’s partially completed Lab 8 tree.',
                  '- `mvn -B clean test` is required to close Lab 8; a warm reactor can hide a cross-module compilation break. Python analytics runs separately.',
                  '- Lab 9 requires X-Upstream diversity before trusting a two-copy result; k6 `run --no-deps` avoids resetting the api service scale.',
                  '- Lab 10 proposed-fix.diff remains unopened until milestone 2. Lab 11 demo predictions precede execution. Lab 12 static/audit findings and staged PR remain part of learning, not preparation repairs.',
                  '- GitHub Actions/fork/PR demonstrations require the learner’s account and explicit publication authorization at execution. If access is blocked, record a recovery task; local tests alone do not prove the required remote CI history.',
                  '- Windows path translation is local and specific; do not provision a second OS, every runtime or a cloud account upfront.']
    write('curriculum/lab-audit.md','\n'.join(lab_lines))
    continuity=['# Assignment continuity and staged release','',
                'Planning document, not a released implementation contract. Detailed future contracts, seeded defects, assessor controls and solutions are not included here. Six public handouts were read in full; the source links below preserve the educational target.','',
                '```text','HW1: isolated intentionally flawed audit system','HW2: new progressive app + core v1 + learner capability contract + harness + ADRs',
                '             ↓ same repository, data and decisions','HW3: evolve/regenerate internals under v2; preserve v1 callers and capability client',
                '             ↓ same application baseline (HW4 is separate)','HW5: v3 replicas + notifications + comparable load evidence; no AWS deploy',
                '             ↓ same v3 system, no new API version','HW6: AWS + CI/CD + telemetry + ≥3.5h operation + incident + teardown',
                'HW4: separate full-history Jenkins snapshot; XML persistence subsystem only','```','',
                'At each prepare/release row, obtain original private inputs only if lawfully available; otherwise create the smallest faithful labeled substitute. Freeze current requirements and acceptance before implementation; hash the source/contract/rubric/evaluator version and baseline commit. Do not release v2/v3 specifics at HW2. Source handouts already expose the themes; the queue controls detailed contract release.','',
                'The official HW2/HW5 handouts permit learner CAPABILITY/NOTIFICATIONS revisions. This reconstruction applies the user’s stricter freeze rule: review learner specifications at the checkpoint, freeze before main build, retain prior versions, and require prospective reviewed ADR/version changes without relaxing released acceptance to fit a solution. Record this adaptation explicitly.','']
    for n,d in HWS.items():
        continuity += [f'## HW{n:02}: {d["title"]}','',f'[Original brief]({source(f"assignments/hw{n}.md")})','',
                       f'- Starting inputs: {d["input"]}',f'- Inaccessible/reconstruction audit: {d["missing"]}',
                       f'- Release responsibility: {d["prep"]}',f'- Checkpoint intent: {d["checkpoint"]}',
                       f'- Final deliverables: {d["final"]}',f'- Independent verification design: {d["acceptance"]}',
                       f'- Published rubric dimensions: {d["weights"]}','']
        write(f'assignments/hw{n:02}/LOCATION.md',f'# HW{n:02} location\n\nReconstructed planning stub; no starter or contract has been released.\n\n'+
              ('Use the same private application repository recorded for HW02. Preserve the preceding accepted commit, contracts, harness, client and decisions.\n' if n in (3,5,6) else 'Working repository: not created. Select at the linked JIT release row. Keep assignment code and transcripts private.\n')+
              f'\nOfficial brief: {source(f"assignments/hw{n}.md")}\n\nRelease/preflight/evaluation prompts are linked from the Excel queue and prompts/INDEX.md. Record the actual repository path and baseline SHA here when that trigger is due.')
        rubric=f'''# HW{n:02} rubric and evidence policy

Original source: {source(f'assignments/hw{n}.md')}

Published dimensions (100 points): {d['weights']}.

Preserve the source brief's individual rubric bullets at the JIT release, linking every point to a frozen criterion and evidence location. This planning summary does not replace the full official rubric. Replace only inaccessible hidden-grader/service components with labeled reconstructed independent checks. Report reconstructed results separately from any official result; never claim grade equivalence.

Required final artifacts: {d['final']}

Verification focus: {d['acceptance']}

Use a result table with criterion/source section, frozen requirement ID, check/reproduction, observed result, evidence path/commit, awarded evidence-based points where applicable, limitations and required recheck. A passing implementation suite alone does not establish harness quality, design judgment or human understanding. An unassessed or blocked item stays explicit. Freeze this expanded rubric and evaluator before learner implementation; do not change the bar after seeing a solution.
'''
        write(f'assessments/rubrics/hw{n:02}.md',rubric)
    continuity += ['## HW4 exact subsystem and historical snapshot','',
                   'Preserve the exact `jenkins-2.568.1` tag and full reachable history. Do not silently substitute a newer Jenkins if the tag cannot be obtained. The public brief describes its tag date as July 9, 2026; verify tag/history at the JIT trigger and record any discrepancy before proceeding. Preserve licenses. The allowlist is `hudson/XmlFile.java`, `hudson/util/XStream2.java`, `XStream2SecurityUtils.java`, three `Robust*Converter.java` files, `hudson/util/xstream/`, `jenkins/util/xstream/`, `AtomicFileWriter.java`, and `hudson/diagnosis/OldDataMonitor.java` under core/src/main/java. Views and everything else are read-only. Copy new tests/fixtures only into the clean evaluator tree, excluding junit-platform.properties and META-INF.','',
                   '## HW6 self-paced operational substitute','',
                   'Replace the inaccessible course-held notifier with a separate assessor-run service exposing only the frozen public protocol. Preserve private fault timing and an independent timestamped service-side record. The learner must really operate for ≥3.5 hours; source dates become ordered start/capture/teardown gates. No fabricated runtime, log evidence or incident is acceptable. Independent hosting/assessment may require the learner to designate a separate operator at that trigger; do not invent one or send messages. No official HW6 oral defense is added.','',
                   '## Carry-forward evidence','',
                   'HW2→3→5→6 carries the same application identity, earlier API contracts, accepted data model/schema, harness, old capability client, frontend, planning/transcripts and append-only decision history. Preserve immutable assignment-baseline commits. Regeneration under HW3 changes implementation, not the compatibility bar or decision history. The separate Jenkins tree never replaces the progressive application.']
    write('curriculum/assignment-continuity.md','\n'.join(continuity))
    for d in LABS:
        n=d['n']
        write(f'labs/lab{n:02}/LOCATION.md',f'# Lab {n:02} location\n\nReconstructed planning stub; this is not a ready environment.\n\n'+
              (f'Archived original: `course-materials/starters/f26-lab{n:02}/`. Treat it as read-only.\n' if n<13 else 'No linked official handout/starter in the pinned snapshot. Refresh or reconstruct only at its queued trigger.\n')+
              f'\nWorking repository: not created. Use `labs/lab{n:02}/work/` or record the learner-selected path here at preparation.\n\nExpected preflight state (unrun): {d["baseline"]}\n\nSee the unit-specific prompts linked in the workbook. Do not execute later labs upfront.')


def more_documents():
    write('curriculum/source-and-gap-register.md',f'''# Source, availability and gap register

Checked 2026-11-23. Public repositories are archived unmodified under `course-materials/`; [source-manifest.json](source-manifest.json) pins commits and every tracked file hash. Those nested upstream checkouts and raw extracted text/previews are locally retained but ignored by the outer git repository. Do not run student work inside them. Retain their licenses; absence of an explicit license is not permission to republish whole teaching decks.

| Source group | Snapshot finding | Local evidence | Operational consequence |
|---|---|---|---|
| [Fall course]({SITE}) | 24 scheduled lecture topics, 21 linked PDFs; 13 labs, 12 public handouts/starters; all six assignment briefs | course-materials/f2026; lecture-page-index.md; lab-audit.md | Plan all topics; source-refresh JITs before four unlinked units |
| [Fall repo](https://github.com/CMU-17-214/f2026) | commit 3f5235eb6a9c652823cb21167846f978eea66c7e | source-manifest.json | Authority for published learning goals, labs, briefs and policies |
| [Spring repo](https://github.com/CMU-17-214/s2026) | commit a5b0b6a349b8b2282d0d42d6de2879a43d704087; public handouts/goals and 25 linked Google lecture decks | course-materials/s2026; spring-deck-downloads.json | Reuse relevant explanations; do not substitute Spring assignments for Fall |
| Spring slide exports | Download/transport state per deck, not a claim that access is guaranteed forever | spring-deck-downloads.json; course-materials/spring-decks/ | Keep original live links and retained public exports; named retry/fallback if transport fails |
| Earlier learner tracker | 50 rows × 15 columns, Checklist and Resource Index, inspected read-only | preserved sibling Spring folder | Use familiar ordered resource/checklist style; improve to a separate stable-ID JIT queue |
| Fall recordings, quizzes and practice/exam papers | Canvas/Panopto/private teaching not supplied | Slide references only; no institutional login attempted | Reconstructed recall checks and separately frozen self-assessments, never claims of recovered exams |
| HW1 original generated app | Private starter not publicly linked by brief | hw1.md | Reconstruct flawed starter at HW1 trigger if unavailable; do not claim exact original README claims |
| HW2 core v1 and course templates | Student-only files absent from public repo | hw2.md | Current-unit labeled core contract at release; two capabilities remain learner designs |
| HW3 v2 and bespoke client | Private additions absent | hw3.md | Freeze v2 at HW3; independent v1 client from the actual frozen HW2 capability |
| HW4 course fork/hidden controls | Public brief specifies upstream tag and subsystem, private course additions missing | hw4.md | Exact history/tag and minimal separately tracked scaffolds at HW4; do not substitute newer code |
| HW5 v3, proxy/load/notifier | Private additions absent | hw5.md | Freeze substitute protocol and comparable scaling procedure at HW5, not now |
| HW6 deploy/traffic/operating service | Private baseline, keyed endpoint and service-side incident record unavailable | hw6.md | Separate assessor-run simulator, actual ≥3.5h block, withheld fault plan and capture-before-teardown |
| Hidden graders and correct/broken implementations | Not recovered | briefs explicitly withhold them | Requirement-derived reconstructed controls kept under assessments/withheld/ |

## Demonstrated instructional gaps and selected support

| Gap and evidence | Fall/Spring coverage judgment | Precise selected resource | Queue placement |
|---|---|---|---|
| Java interface/visibility reading is assumed in L03 and Maven starters | Spring OO basics/Inheritance and Delegation deepen it; no full Java course needed | [Java classes/objects]({EXTERNAL['java'][1]}) and the exact Spring deck links in concept-map.md | SUP-JAVA before Lab 1; SUP-COMPOSITION before L10, conditional |
| HTTP status/path vocabulary needed before HW1; brief explicitly points to MDN | Fall L11 comes later | [MDN status codes]({EXTERNAL['http'][1]}) | SUP-HTTP before HW1 |
| Fake/stub/mock distinctions and unit syntax | Fall L03 supplies design; Spring Testability and Lab 7 supply alternate definitions | [Spring Test Doubles]({SPRING}labs/lab07.md) | SUP-DOUBLES after L03 if needed |
| Property library syntax differs between Lab 2 and HW1 | Fall L04 explains properties, shrinking and limits; Spring Test Case Design provides conventional techniques | [jqwik 1.8.4]({EXTERNAL['jqwik'][1]}); [fast-check core blocks]({EXTERNAL['fastcheck'][1]}) | SUP-JQWIK before Lab 2, SUP-FASTCHECK before HW1 repair |
| Lab 6 is before Fall API lecture | Its handout already teaches additive/breaking/deprecation | [Lab 6 primer]({FALL}labs/lab06.md#some-concepts-that-will-be-helpful) | SUP-LAB06-API, no invented full prerequisite course |
| Agent architecture/supervision/context/memory allegedly missing | Actually covered substantially in L02, L06, L12, L13, L14; Spring has no equivalent agent units | [MCP participants/layers]({EXTERNAL['mcp'][1]}) only for current protocol boundary | SUP-MCP; no redundant external agent curriculum |
| Personal AWS differs from Academy setup in Lab 3/4 and HW6 | Lab 4 starter hard-codes Academy IAM/key/default-network assumptions | [SSM permissions]({EXTERNAL['awsssm'][1]}), [identity]({EXTERNAL['awsidentity'][1]}), [Budgets]({EXTERNAL['awsbudget'][1]}), [pricing]({EXTERNAL['awsprice'][1]}) | AWS readiness and exact-unit provisioning/teardown JITs |
| Replica load mechanics require CLI/threshold interpretation | L16 teaches state, curves, measurement blind spots; Spring distributed robustness reinforces concepts | [Compose up/scale]({EXTERNAL['compose'][1]}); [k6 thresholds]({EXTERNAL['k6'][1]}) | SUP-COMPOSE before Lab 9/HW5 |
| Python tooling is needed for later mixed-language labs | L21 provides static/dynamic concepts, not full environment setup | [Python venv]({EXTERNAL['venv'][1]}) | Lab 8/9 preparation; SUP-PYTHON before Lab 12 |
| L22 Fall PDF unlinked | Spring Supply Chain Security deck is the first fallback; inspect availability at trigger | [SLSA threats]({EXTERNAL['slsa'][1]}) only for remaining provenance gap | LEC22 source refresh and reconstructed guide |
| L23 monitoring PDF unlinked and HW6 demands telemetry-only incident reasoning | HW6 defines outputs but does not replace a full explanation; no Spring monitoring lecture | [Google SRE Ch.6]({EXTERNAL['sre'][1]}); [OpenTelemetry signals]({EXTERNAL['otel'][1]}) | LEC23 source refresh and reconstructed guide before operating block |
| L24 and Lab13 material unlinked | Official goals/title give scope, not private handout details | [Fall learning goals]({FALL}learninggoals.md) and HW6 telemetry requirements | Individual refresh/fallback tasks before synthesis and Lab13 |

All judgments are reconstructed instructional analysis. A source being inaccessible is different from the source teaching a concept inadequately. No missing original material is asserted recovered. Resource links and downloads are validated separately in reviews/package-validation.md and curriculum/link-audit.json; live transport failures remain explicit.

The [Spring cross-reference](spring-cross-reference.md) gives inspected section/page references and a full export inventory. Spring DevOps has a brief monitoring overview (PDF pages 59–63); it does not supply HW6's full telemetry-only localization method, which is why the SRE reading is selected. Static starter manifest/workflow evidence is retained in [starter-static-audit.json](starter-static-audit.json). Seven failed GitHub file-view routes were replaced by verified raw-file URLs at the same pinned commit; original failures and fallback checks remain recorded in link-audit.json, link-fallback-checks.json and source-link-overrides.json.
''')
    write('curriculum/reconstructed-study-guides.md',f'''# Reconstructed guides for currently unlinked Fall units

These are newly authored study instructions, not official Fall slides. Each queued source-refresh prompt first checks for newly published official material. If available, use and analyze it instead; preserve the historical snapshot and frozen assignment obligations.

## LEC-22: Supply Chain Security

First use the [Spring Supply Chain Security lecture]({SPRING_DECKS['Supply Chain Security']}) as the CMU explanation. Read its dependency/transitive-dependency, malicious-package, maintainer and build-access examples. Where build provenance remains unclear, read [SLSA v1.2 threats overview]({EXTERNAL['slsa'][1]}): identify who can change source, dependencies, workflow and built output. Do not confuse a clean vulnerability audit with proof that a package is trustworthy.

Draw your HW6 build chain: source → dependencies/actions → builder → image registry → deployed instance. Label one trust decision and one evidence artifact at each edge. Explain lockfiles versus immutable digests, least-privilege workflow credentials, and why secret scanning cannot revoke an already exposed secret. Use [GitHub secure workflow guidance]({EXTERNAL['actions'][1]}) only for your remaining workflow-specific questions. Leave gate implementation to the assignment.

Done when your notes cite the Spring pages actually read, distinguish known-vulnerability, malicious-content and provenance checks, and explain one threat your current gates cannot detect. If the Spring export is unavailable, record the access failure and use SLSA plus GitHub guidance as the labeled reconstructed explanation; do not report having read the deck.

## LEC-23: Observability and Monitoring

Read [Google SRE, Chapter 6]({EXTERNAL['sre'][1]}), specifically Definitions, Symptoms Versus Causes, Black-Box Versus White-Box, The Four Golden Signals, and As Simple as Possible, No Simpler. Read [OpenTelemetry signals]({EXTERNAL['otel'][1]}) to distinguish logs, metrics and traces. This fills the unlinked Fall lecture without requiring an observability vendor stack.

For your own HW6 design, identify a user-visible symptom, an appropriate metric, a threshold/window and an alert action. Sketch a single DM from acceptance through notification attempt to outcome using request/message identifiers and timestamps. Explain what evidence distinguishes your service failing from the notifier failing; a 202 acceptance alone cannot establish delivery. Write which silent failures your public observation interface can and cannot detect. Never log the keyed NOTIFY_URL.

Done when the notes explain a telemetry-only request trace, a meaningful user-impact alert and at least one uncertainty; the actual implementation and alert demonstration remain learner work.

## LEC-24: Summary and What We Learned Together

Use the [official learning goals]({FALL}learninggoals.md), your six immutable assignment reviews and lab records. For verification, change/reuse, scale/operations, agent supervision, engineering memory and unfamiliar-code reasoning, point to one concrete personal artifact and one remaining weakness. Revisit one HW2 founding decision, its HW3/HW5 supersession and its HW6 operational consequence; keep the original ADR intact.

Done when each goal has evidence or a named gap, and the learner can explain one counterexample to an overly broad success claim without an agent.

## Lab 13 release design (not a ready starter)

At its queued refresh, prefer the actual official handout and repo. If absent, the preparation agent writes a labeled reconstructed three-milestone lab: (1) correlate a request with logs and a behavior-sensitive metric, (2) demonstrate an alert on a reproducible user-visible fault, (3) localize the failure and explain an observation blind spot. Reuse the learner’s HW6 artifacts or a minimal healthy local service; avoid a new billable stack. Freeze exact milestones and expected evidence before setup. Do not provide the fault diagnosis, instrumentation solution or private fault schedule in learner-facing instructions.
''')
    write('assessments/rubrics/assessment-policy.md',f'''# Reconstructed assessment policy

Authority: [Fall policies]({FALL}policies.md), [lab policy]({FALL}labs.md), each complete assignment brief and [learning goals]({FALL}learninggoals.md). Official course weights are assignments 50%, exams 30% (7.5/7.5/15), labs 10%, participation 10%. These describe the original course, not an independently awarded CMU grade. No letter-grade equivalence is claimed.

- Labs preserve all three milestones and a learner-only explanation. Record completeness, evidence quality, uncertainty and needed corrections; an assistant saying “pass” is not TA signoff.
- HW1–6 use their published point dimensions and item-level criteria expanded/frozen at each release. Inaccessible staff-suite points are assessed with explicitly reconstructed independent controls, never silently awarded from the learner suite. HW4 defense checks correctness; HW1/2/3/5 defenses check a meaningful conversation. HW6 has no official defense.
- A requirement matrix includes stable requirement ID, source section/page, official/adapted/reconstructed label, version/hash, public acceptance obligation, independent verification method and evidence link. Assessor-only cases and seeded defects remain outside learner prompts.
- Record pass/fail/blocked/unassessed separately. Explain how a check could be green and wrong. Reproduce significant findings with an input, command, trace or counterexample. Review APIs, data ownership, scope, architecture, test oracles, ADR truth and supervision history, not just counts.
- Critique design using alternatives and priced quality attributes. Ask a counterfactual (“what changes if this assumption fails?”), and compare the answer with actual code. Require learner responses before providing any critique that would answer the question for them.
- Independent harness assessment uses controlled conforming and nonconforming behavior under the frozen contract; characterize tests are run on both original and restructured implementations. Retain controls separately and validate them independently before using their verdicts.
- Freeze core and acceptance criteria before learner implementation. Freeze learner-specified capabilities/policies at the checkpoint before main implementation. A prospective clarification keeps old requirements and clients, records an ADR/version and updates criteria before affected work; never retrofit a criterion just to accept a solution.
- Reconstructed midterms/final assess unseen reasoning under frozen scope. Exams, lab explanations and defenses are unassisted. Recall notes after every lecture replace unavailable in-class quizzes without pretending to reproduce them.
- Self-assessment cannot reproduce an independent institutional grader. Keep question papers, answer keys, scenario schedules and expected findings under assessor control where possible; disclose when the learner operates both roles.

Review output: source/revision and assessed commit; item-to-evidence matrix; commands/results and environment; scope/test/architecture/memory/process critique; unassisted question/response; uncertainties; concrete findings/rechecks; cleanup verdict. Keep original evidence and correction history distinct.
''')
    write('assessments/withheld/README.md','''# Assessor-only boundary

No tests, defect registry, solution or answer key have been built upfront. Prepare only the current unit at its queued assessor task. Keep intentional defect descriptions, correct/broken controls, future contract details, exam keys and HW6 fault timing/service records here or in a separate private assessor repository. Do not expose them in learner prompts or source summaries.

This directory name is an accidental-spoiler boundary, not an access-control mechanism. Use a separate session/repository/operator for independence where possible. Label all locally authored checks reconstructed; no CMU hidden suite has been recovered.
''')
    write('progress/decisions.md','''# Reconstruction decisions

## D001 — 2026-11-23: source snapshot and ordering

Use pinned Fall public materials as authority, Spring as targeted explanation and primary external references only for demonstrated gaps. Preserve the scheduled sequence without calendar deadlines. Archive originals separately; install exercise runtimes only at queued triggers. The earlier Spring tracker was inspected read-only and preserved.

## D002 — 2026-11-23: staged contracts and one evolving application

HW1 is separate; HW2/3/5/6 use one application/repository and accumulated contracts, frontend, tests, harness, client and accepted ADRs. HW4 is a separate exact-history Jenkins tree. Freeze only current-unit detailed requirements; future implementations and hidden assessment resources are deferred.

## D003 — 2026-11-23: unavailable instruction and assessment

Do not infer hidden starters, recordings, exams or tests from their titles. Missing L22–24/Lab13 each have a source-refresh row and a labeled fallback. Reconstructed recall and frozen unassisted exams replace inaccessible classroom participation for self-study; they carry no institutional grade equivalence.

## D004 — 2026-11-23: freeze learner-selected obligations

The user requires frozen acceptance before implementation. The original HW2/HW5 briefs allow CAPABILITY/NOTIFICATIONS changes. Keep the core contract frozen at release, freeze learner choices after checkpoint review before main build, and preserve versioned prospective changes with ADRs and previous compatibility obligations. Do not relax acceptance to fit a solution. This is a deliberate self-study adaptation.

## D005 — 2026-11-23: personal AWS and actual operation

Replace Academy identities/profiles/key/budget assumptions only when current units need them. Pair each billable provisioning task with an explicit teardown row. Preserve Lab4's deliberate scenario. HW6 retains a real ≥3.5-hour block and independent service record with withheld fault timing while replacing semester calendar dates. No resources have been provisioned by curriculum construction.

## D006 — 2026-11-23: honest review boundaries

Deck analysis is text-led across all published decks, supported by full page extraction, page inventory, targeted examples and selected rendered visuals. Do not describe it as exhaustive visual inspection or recovered live teaching. Static starter audit does not prove any local runtime is ready. Technical package validation, runtime readiness and learner mastery remain separate.
''')
    write('progress/change-log.md','''# Change log

- 2026-11-23 — Constructed the source-pinned Fall self-study curriculum, deck/topic/prerequisite analysis, public lab/private-assignment audits, staged continuity and assessment policy. Authored individual JIT prompts and a single ordered Excel queue. Preserved the earlier Spring workspace. No learner exercise was solved, no exercise environments were installed or executed, and no cloud resources were created. Package verification evidence is in reviews/package-validation.md.
''')
    write('progress/cloud-resources.md','''# Cloud resource ledger

No cloud resources were created during curriculum construction. Fill this ledger at the exact-unit provisioning trigger.

| Unit / provision row | Profile / redacted account / role | Region | Template and plan hash | Resource type and exact ID | Tags | Start / approved duration | Estimated and actual cost | Evidence capture | Matching teardown row | Removed / retained proof |
|---|---|---|---|---|---|---|---|---|---|---|

Personal AWS has no assumed Academy budget enforcement. Include instances, volumes, public IPs, retained storage/logs, registry images, networking and assessor-side services. Approval to delete covers an exact verified inventory; capture evidence before removing it. A stop timer or budget alert does not guarantee zero charges.
''')
    write('README.md','''# CMU 17-214/514 Fall 2026 self-study reconstruction

Open [the Excel execution queue](syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx). The first unfinished row is the next action. There are no compulsory dates. Preparation, learning, independent verification, correction and cleanup are separate rows; use each JIT row’s saved prompt in a fresh working session.

1. Open the workbook’s Start sheet, then the Queue table. Inspect its first unfinished row and dependencies.
2. For a JIT row, follow Saved prompt, supply the listed paths/commits and execute only that operation. For a learning row, study or do the exercise yourself under the course’s supervision rules.
3. Record Status and Evidence in that same row. A blocked task gets a named recovery row/prompt before the dependent activity; do not skip it. Save pending row-ID updates if Excel locks the file.

The initial reconstruction plans the full course; it does not prepare every runtime, build every starter, solve exercises or deploy cloud resources upfront. Detailed assignment requirements and independent controls are released/frozen only when their prompts come due. The learner still has to complete every study and assessment activity.

- [Prompt index](prompts/INDEX.md): every saved JIT operation, trigger and expected output.
- [Concept/prerequisite map](curriculum/concept-map.md) and [lecture analysis](curriculum/lecture-review.md).
- [Source/gap register](curriculum/source-and-gap-register.md), [lab audit](curriculum/lab-audit.md), [assignment continuity](curriculum/assignment-continuity.md).
- [Reconstructed guides for unlinked units](curriculum/reconstructed-study-guides.md).
- [Assessment policy](assessments/rubrics/assessment-policy.md), [decisions](progress/decisions.md), [change log](progress/change-log.md).
- [Package validation](reviews/package-validation.md): checks actually performed, live-source limits and next action.

Original public materials remain unmodified in local `course-materials/f2026/`, `s2026/`, `spring-decks/` and `starters/`. These downloaded nested repositories, PDF text/previews and analysis dependencies are ignored by the outer git repo. [source-manifest.json](curriculum/source-manifest.json) records original commits and hashes; [spring-deck-downloads.json](curriculum/spring-deck-downloads.json) records export availability. Do not redistribute copied teaching resources without checking their licenses. Keep learner code in unit working repositories, not source archives. The existing Spring course folder and tracker remain unchanged.

All new guides, prompts, workbook ordering adaptations and replacement assessment designs are **reconstructed**. Public CMU handouts are the target, not evidence that private starters, recordings or hidden graders were recovered. Results are independent self-study evidence, not official CMU grades or equivalence.

Reproduce the package structure check with `python tools/validate_package.py`. Generation uses `tools/course_data.py` and `tools/build_package.py`; after learning starts, preserve workbook status/evidence and review changes by stable ID. Source downloads/review helpers require locally installed dependencies and network authorization; they never execute exercise preparation.
''')


def workbook():
    old={}
    if BOOK.exists():
        wb=load_workbook(BOOK)
        for values in wb['Queue'].iter_rows(min_row=2,values_only=True):
            old[values[1]]=values
    wb=Workbook(); start=wb.active;start.title='Start';queue=wb.create_sheet('Queue'); res=wb.create_sheet('Resources'); coverage=wb.create_sheet('Coverage')
    start_rows=[['Fall 2026 independent self-study','Reconstructed execution queue — source snapshot 2026-11-23'],
                ['Next action','Open Queue: the first unfinished row. Never skip a blocked row.'],
                ['Next unfinished ID',f'=IFERROR(INDEX(Queue!B2:B{len(rows)+1},MATCH(FALSE,INDEX(Queue!M2:M{len(rows)+1}="Complete",0),0)),"All rows complete")'],
                ['Next unfinished action',f'=IFERROR(INDEX(Queue!D2:D{len(rows)+1},MATCH(FALSE,INDEX(Queue!M2:M{len(rows)+1}="Complete",0),0)),"Review final reconciliation")'],
                ['Statuses','Not started / Ready / In progress / Blocked / Complete'],
                ['Ready','Prerequisites and inputs checked; does not claim exercise completion. Only first row is initially Ready.'],
                ['Execute a JIT row','Open its Saved prompt, supply inputs, perform only that task, record actual evidence and update the row.'],
                ['Blocked recovery','Record cause. Insert a new stable-ID recovery JIT row and saved prompt before the dependent activity; complete recovery and original row before advancing.'],
                ['Frozen acceptance','Release current assignment requirements before implementation; freeze learner specifications at checkpoint before main build; keep old versions/clients.'],
                ['Privacy','Assignment code/transcripts private. Lab transcripts local/uncommitted. Assessor checks, defects and scenario timing stay separate.'],
                ['Cloud','No upfront deployment. Every provisioning step has a teardown row; personal-account budget alerts/timers are not billing caps.'],
                ['Source coverage','21 published Fall PDFs; all 24 scheduled lecture topics, 13 labs and six assignments mapped. Unlinked units have refresh/fallback rows.'],
                ['Validation','See ../reviews/package-validation.md. Structural workbook checks do not prove exercise runtime readiness or learning mastery.'],
                ['Excel file lock','Save row-ID-based pending updates under progress/pending-updates/; reconcile them before the next row.'],
                ['Link behavior','Source cells point to exact official resources; Saved prompt links are relative to this workbook. Keep syllabus/ and prompts/ together.'],
                ['Reconstructed status','No official grade equivalence; no hidden CMU grader or private teaching material recovered.']]
    for row in start_rows: start.append(row)
    start.column_dimensions['A'].width=28;start.column_dimensions['B'].width=112
    for row in start:
        start.row_dimensions[row[0].row].height=48
        for c in row: c.alignment=Alignment(wrap_text=True,vertical='top')
    start['B13'].hyperlink='../reviews/package-validation.md';start['B13'].style='Hyperlink'
    queue.append(HEADERS)
    for r in rows:
        values=[r[h] for h in HEADERS]
        if r['ID'] in old:
            # These fields are learner progress, never regenerated from curriculum metadata.
            for col in (12,13,14): values[col]=old[r['ID']][col]
            r['Status / Complete'],r['Evidence / output link'],r['Notes']=values[12:15]
        for pair in json.loads((ROOT/'curriculum/cloud-task-pairs.json').read_text()):
            if r['ID']==pair['provision'] and pair['teardown'] not in (values[14] or ''):
                values[14]=(values[14] or '')+f' Matching mandatory teardown: {pair["teardown"]}.'
        queue.append(values)
        idx=queue.max_row
        for col in (6,7,10):
            v=values[col-1]
            if v:
                queue.cell(idx,col).hyperlink=v
                queue.cell(idx,col).style='Hyperlink'
        if values[13] and (str(values[13]).startswith(('http','../'))):
            queue.cell(idx,14).hyperlink=values[13];queue.cell(idx,14).style='Hyperlink'
        queue.row_dimensions[idx].height=100 if r['Activity type'].startswith('JIT') else 125
        for c in queue[idx]: c.alignment=Alignment(wrap_text=True,vertical='top')
    widths=[8,22,24,52,62,34,34,23,48,38,64,78,17,38,80]
    for i,width in enumerate(widths,1): queue.column_dimensions[chr(64+i)].width=width
    queue.freeze_panes='E2';queue.sheet_view.zoomScale=70
    table=Table(displayName='ExecutionQueue',ref=f'A1:O{queue.max_row}');table.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showRowStripes=True);queue.add_table(table)
    validation=DataValidation(type='list',formula1='"Not started,Ready,In progress,Blocked,Complete"',allow_blank=False)
    validation.error='Choose a listed status.';validation.errorTitle='Controlled status';validation.showErrorMessage=True;validation.errorStyle='stop';queue.add_data_validation(validation);validation.add(f'M2:M{queue.max_row}')
    for status,color in [('Complete','DFF0D8'),('Blocked','F8D7DA'),('In progress','FFF3CD'),('Ready','D9EDF7')]:
        queue.conditional_formatting.add(f'A2:O{queue.max_row}',FormulaRule(formula=[f'$M2="{status}"'],fill=PatternFill('solid',fgColor=color)))
    queue.auto_filter.ref=table.ref
    queue.print_title_rows='1:1';queue.page_setup.orientation='landscape';queue.page_setup.paperSize=queue.PAPERSIZE_A3;queue.page_setup.fitToWidth=1;queue.sheet_properties.pageSetUpPr.fitToPage=True
    queue['J1'].comment=Comment('Relative links resolve from syllabus/. Each JIT row must point to its own existing Markdown file.','Reconstruction')
    res.append(['ID','Resource / provenance','URL or local path','Use / scope'])
    entries=[('FALL-SITE','Original CMU Fall schedule and policies',SITE,'Authority; recheck newly published units'),
             ('FALL-GOALS','Original Fall learning goals',source('learninggoals.md'),'All objectives'),
             ('FALL-POLICY','Original Fall agent policy',source('policies.md'),'Transcript, privacy, supervision'),
             ('SPRING-SITE','Original CMU Spring course','https://cmu-17-214.github.io/s2026/','Reference only')]
    entries += [(f'EXT-{k}',name,url,'Primary external reference; see source-and-gap-register.md') for k,(name,url) in EXTERNAL.items()]
    entries += [(f'SPR-{i:02}',name,url,'Original CMU Spring slide deck; targeted support or conditional prerequisite') for i,(name,url) in enumerate(SPRING_DECKS.items(),1)]
    entries += [(f'FALL-L{i:02}',d[1],source(f'slides/{d[0]}.pdf'),'Original Fall deck; see lecture-review.md') for i,d in enumerate(LECTURES,1)]
    entries += [(f'FALL-LAB{d["n"]:02}',d['title'],source(f'labs/lab{d["n"]:02}.md'),'Original public lab handout') for d in LABS if d['n']<13]
    entries += [(f'FALL-HW{n:02}',d['title'],source(f'assignments/hw{n}.md'),'Original assignment brief; private files audited separately') for n,d in HWS.items()]
    entries += [(f'REPO-LAB{n:02}',f'Original public Lab {n:02} starter',f'https://github.com/CMU-17-214/f26-lab{n:02}','Archived SHA in source-manifest.json; working copy only at JIT trigger') for n in range(1,13)]
    for row in entries:
        row=tuple(resolve_source_links(v) if isinstance(v,str) else v for v in row)
        res.append(row);res.cell(res.max_row,3).hyperlink=row[2];res.cell(res.max_row,3).style='Hyperlink'
    resources.extend([dict(id=e[0],name=e[1],url=e[2],use=e[3]) for e in entries])
    for col,width in zip('ABCD',[22,65,105,85]):res.column_dimensions[col].width=width
    res.freeze_panes='C2';rt=Table(displayName='ResourceCatalog',ref=f'A1:D{res.max_row}');rt.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showRowStripes=True);res.add_table(rt)
    coverage.append(['Unit','Original / reconstructed availability','Evidence reference'])
    for i,d in enumerate(LECTURES,1):coverage.append([f'LEC-{i:02}','Original published PDF; text-led analysis and selected visuals','../curriculum/lecture-review.md'])
    for i in (22,23,24):coverage.append([f'LEC-{i:02}','Unlinked in snapshot; individual source-refresh then labeled fallback','../curriculum/reconstructed-study-guides.md'])
    for d in LABS:coverage.append([f'LAB-{d["n"]:02}','Original handout/starter statically audited' if d['n']<13 else 'Unlinked; source-refresh then labeled reconstruction at trigger','../curriculum/lab-audit.md'])
    for n in HWS:coverage.append([f'HW-{n:02}','Original brief; private resources reconstructed JIT only','../curriculum/assignment-continuity.md'])
    coverage.column_dimensions['A'].width=18;coverage.column_dimensions['B'].width=85;coverage.column_dimensions['C'].width=65;coverage.freeze_panes='B2'
    for s in (res,coverage):
        for row in s.iter_rows(min_row=2):
            s.row_dimensions[row[0].row].height=42
            for c in row:c.alignment=Alignment(wrap_text=True,vertical='top')
    for r in range(2,coverage.max_row+1):coverage.cell(r,3).hyperlink=coverage.cell(r,3).value;coverage.cell(r,3).style='Hyperlink'
    for sheet in wb:
        for cell in sheet[1]:cell.fill=PatternFill('solid',fgColor='183A5A');cell.font=Font(color='FFFFFF',bold=True);cell.alignment=Alignment(wrap_text=True,vertical='center')
        sheet.row_dimensions[1].height=34
    BOOK.parent.mkdir(exist_ok=True)
    wb.save(BOOK)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--rebuild',action='store_true');args=parser.parse_args()
    if BOOK.exists() and not args.rebuild:raise SystemExit('Workbook exists. Inspect progress and use --rebuild explicitly; stable-ID status/evidence/notes are preserved.')
    make_queue()
    # Resolve explicit, stable provisioning→teardown pairs after all IDs are allocated.
    pair_keys=[('lab04-provision','lab04-cleanup'),('hw02-deploy','hw02-teardown'),
               ('hw06-checkpoint-deploy','hw06-checkpoint-teardown'),
               ('hw06-operating-service','hw06-operating-teardown'),('hw06-operating-deploy','hw06-operating-teardown')]
    pairs=[]
    for provision_key,teardown_key in pair_keys:
        provision,teardown=id_map[provision_key],id_map[teardown_key]
        pairs.append(dict(provision=provision,teardown=teardown))
        row=next(r for r in rows if r['ID']==provision)
        row['Notes']+=f' Matching teardown: {teardown}; both learner and assessor resource inventories are included where applicable.'
        prompt=next(p for p in prompts if p['id']==provision)
        path=ROOT/prompt['file']
        path.write_text(path.read_text(encoding='utf-8')+f'\nMatching mandatory teardown queue row: **{teardown}**. Record this exact ID in the resource ledger before provisioning.\n',encoding='utf-8')
    write('curriculum/cloud-task-pairs.json',json.dumps(pairs,indent=2))
    documents()
    more_documents()
    workbook()
    write('prompts/task-id-map.json',json.dumps(id_map,indent=2))
    write('curriculum/course-plan.json',json.dumps(rows,indent=2,ensure_ascii=False))
    write('curriculum/resource-catalog.json',json.dumps(resources,indent=2,ensure_ascii=False))
    index=['# Saved JIT prompt index','',
           'Open the workbook row first. Follow its direct Saved prompt link, supply the listed persistent inputs, execute only that task, then record status and evidence in the same row. These prompts are reconstructed operational instructions, not exercise solutions. Prompt IDs and row IDs are identical and stable.','',
           '| Prompt ID | Syllabus row | Trigger | Saved file | Purpose | Required output |','|---|---|---|---|---|---|']
    for p in prompts:
        index.append(f'| {p["id"]} | {p["row"]} | {p["trigger"]} | [{Path(p["file"]).name}]({Path(p["file"]).name}) | {p["purpose"]} | {p["output"]} |')
    write('prompts/INDEX.md','\n'.join(index))
    print(json.dumps({'queue_rows':len(rows),'jit_prompts':len(prompts),'resources':len(resources),'workbook':str(BOOK)}))


if __name__=='__main__':main()
