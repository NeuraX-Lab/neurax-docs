# V5 verification / publication receipt
Status: V5_HANDOFF_VERIFIED. See machine manifest for exact compatible payload pins, tree IDs, Git-blob SHA256, V4.1 baselines and log hashes.

| Verification | Actual outcome |
|---|---|
| Three remotes/branches | Created without force/main merge; clone from GitHub succeeded |
| Access Am2uocVi3t | Read allthree incl private lab; write docs only; no permission mutation |
| Fresh dependency installation | npmci305packages + newPythonvenv; add existing optionalrasterio for full suite |
| Backend |47PASS; existing Starlette/httpx deprecation retained |
| Frontend |21PASS;typecheck/lint/buildPASS |
| Browser/integration |26PASS, including ten original V4 acceptance scenarios |
| D1/Q1/EDA |132monthly rows and source flag retained; no-fit verifier PASS; local raw checksum/reconstruction PASS |
| Model/E1 | Existing24predictions reproduce MAE/RMSE; no new research model; RESEARCH_ONLY/no production consumer |
| A1 shared run and unsupported AOI | Browser and backend scenarios PASS; no borrowed MyThanh cache |
| Production inference exclusion | Actual HTTP409 with research artifact;404 absent; tested |
| H1 monitoring and field exclusion | Actual endpoint/UI synthetic/mock/replay tests PASS; physical device NOT_TESTED |
| Assets/history/WIP | New reachable blobs scanned; rights-reviewed plot/terrain only; docs unsafe unpublished history excluded;18WIPfiles unchanged |
| Mentor/science/user study | Mentor decisionsOPEN; external agronomic approval/field measurements/user study not asserted |

Initial cleanbackend collection failed because coverage tests import rasterio; setup instructions now explicitly install the declared optional dependency, then all47passed. No tests skipped/deleted. Fresh installedFastAPI0.162.7 vs baseline0.162.5; code remains compatible. npm11.6.2 bootstrap tarball integrity checked; system PATH and original env not modified. Clean-clone full runtime code matches payloads; later lab changes are handoff text only.

Model weights and original raw/imagery caches not distributed. Artifact/text hashes use recorded Git-blob/LF identity where checkout newline conversion matters; historical V4.1raw-byte receipts remain unchanged. Scientific metrics/schema/source content verified separately. This is a verified handoff, not stronger field/model/agronomic validation.

Việt: read START_HERE_FOR_VIET on lab pin, discuss mentor packet, fill decisionlog, create separate research branch. Obtain write/privatefork approval before pushing lab/product research. AI→evidence→contractreview→PR→backend/frontendtests→Hưngreview→merge. Hưng can develop product UX/demo/pitch against pinned sharedA1 in parallel.

Original dirty docs checkout remains checkpoint/v5-viet-unsanitized; safe docs handoff is a separate worktree/remote branch. No old history rewritten, no local data deletion, no account permission change, no external teammate message. Temporary verification services stopped after checks.
