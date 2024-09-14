SCRIPT_DIR="$(dirname "$0")"

source "$SCRIPT_DIR"/.venv/bin/activate

streamlit run $SCRIPT_DIR/main.py
