#!/usr/bin/env bash
# Reconstruct the swmm-brain workspace on any machine: clone (or update) the
# curated knowledge repos as sibling subfolders of this script.
#
#   chmod +x setup.sh && ./setup.sh
#
# Each entry is "owner/repo". The folder name is the repo name. Cloning side by side
# does NOT entangle the repos — each keeps its own independent .git history.
set -euo pipefail

# ============================================================================
#  EDIT THIS LIST. Active = pulled in. Commented (#) = available, uncomment to add.
# ============================================================================
REPOS=(
  # --- active default set: knowledge substrate ---
  Dickinsonre/rdickinson-rdickinson          # life's work, SWMM + ICM
  Dickinsonre/AWI_RED_Combined               # consolidated Ruby/source toolkit
  Dickinsonre/InfoWorks-ICM-Ruby-Scripting-  # ICM Ruby resources + examples
  Dickinsonre/ICM_Tools                      # ICM SQL + Ruby helper scripts
  Dickinsonre/Innovyze-ICM-Libraries         # open ICM libraries + docs
  Dickinsonre/SwmmHistory                    # SWMM5 history

  # --- uncomment any of these to include them ---
  # Dickinsonre/Understand-Anything          # teaching-graphs from code
  # Dickinsonre/inventing-memory             # memory / knowledge-graph work
  # Dickinsonre/HistoricalWaterInventions    # history of water inventions
  # Dickinsonre/ruby_scripts                 # loose Ruby scripts
  # Dickinsonre/Open-Source-Support          # open code from Innovyze era
  # Dickinsonre/ReSWMM                        # read/edit SWMM .inp engine
  # Dickinsonre/InfoSewer-to-ICM             # InfoSewer -> ICM/SWMM networks
  # Dickinsonre/EPANET-SWMM5-Generate        # EPANET <-> SWMM5 generation
  # SWMMEnablement/bobswmmapps               # index of Bob's browser apps
  # SWMMEnablement/rulesforresponsiblemodeling
  # SWMMEnablement/epa-swmm5-essentials      # core SWMM5 concepts, one reference
  # SWMMEnablement/.github                    # org profile / community files

  # --- any GitHub repo works: add "owner/name" ---
)

# ============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Workspace: $SCRIPT_DIR"
echo

for entry in "${REPOS[@]}"; do
  name="${entry##*/}"
  if [ -d "$name/.git" ]; then
    echo "↻ $name  (updating)"
    git -C "$name" pull --ff-only || echo "    pull skipped (diverged or local changes)"
  elif [ -d "$name" ]; then
    echo "• $name  (folder exists, not a git repo — skipping)"
  else
    echo "↓ $entry  (cloning)"
    git clone --quiet "https://github.com/$entry.git" "$name"
  fi
done

echo
echo "Done. Start the brain:  claude     (from $SCRIPT_DIR)"

# Notes:
#  - HTTPS clone works on a fresh machine with no SSH key. For a PRIVATE notes
#    repo, either clone it manually here or switch its line to git@github.com:...
#  - Want speed over full history? Add  --depth 1  to the git clone line above.
#    (History is the point for legacy work, so the default is a full clone.)
