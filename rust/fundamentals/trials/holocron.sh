#!/bin/bash

DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="${DIRECTORY}/src/bin"
mkdir -p "$BIN_DIR"

show_help() {
  echo "🦀 HOLOCRON RS - Your guide in the Jedi Academy (Rust)"
  echo "----------------------------------------------------------"
  echo "Usage:"
  echo "  ./holocron.sh -m \"ID. Name\"  -> [M]editate: Create new Trial"
  echo "  ./holocron.sh -t <ID>          -> [T]rain: Run Trial tests"
  echo "  ./holocron.sh -r <ID> [case]   -> [R]un: Execute Trial main (optional test case index)"
  echo "  ./holocron.sh -l               -> [L]og: List completed Trials"
  echo ""
  echo "Examples:"
  echo "  ./holocron.sh -m \"1. Two Sum\""
  echo "  ./holocron.sh -t 1"
  echo "  ./holocron.sh -r 1"
  echo ""
  echo "Runs from anywhere: rust/fundamentals/trials/holocron.sh -t 1"
  exit 1
}

if [ $# -eq 0 ]; then
  show_help
fi

OPTION=$1
VALUE=$2

case $OPTION in
-m | --meditate)
  INPUT=$VALUE
  NUMBER=$(echo "$INPUT" | grep -oE '^[0-9]+')
  PROBLEM_NAME=$(echo "$INPUT" | sed -E 's/^[0-9]+\.? *//')
  PACKAGE_NAME=$(echo "$PROBLEM_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 ]//g' | sed 's/  */_/g' | sed 's/ /_/g')

  if [ -z "$NUMBER" ] || [ -z "$PROBLEM_NAME" ]; then
    echo "❌ Error: Invalid format. Use \"ID. Name\""
    exit 1
  fi

  BIN_NAME="${NUMBER}_${PACKAGE_NAME}"
  BIN_FILE="${BIN_DIR}/${BIN_NAME}.rs"

  if [ -f "$BIN_FILE" ]; then
    echo "⚠️  This Trial already exists in the Academy. Keep training, Padawan!"
  else
    cat <<EOF >"$BIN_FILE"
use colored::*;
use katas::s;

struct Solution;

/**
 * Solución a implementar
 */
impl Solution {
    pub fn ${PACKAGE_NAME}() {
        todo!()
    }
}

/**
 * Casos de prueba
 *
 * casos borde:
 * E1. ...
 */
fn get_test_cases() -> Vec<(/* input, expected */)> {
    vec![
      // /**/ (, ), // E
    ]
}

/**
 * Ejecución a discresión
 */
fn main() {
    const DEFAULT: usize = 0;

    let suite = get_test_cases();
    let idx: usize = std::env::var("TRIAL_CASE")
        .ok()
        .and_then(|v| v.parse().ok())
        .unwrap_or(DEFAULT);

    let (input, expected) = &suite[idx];
    let answer = Solution::${PACKAGE_NAME}(/* input */);
    println!(
        "answer: {} | expected: {}",
        format!("{}", answer).green().italic().underline(),
        format!("{}", expected).blue().italic().underline()
    );
}

/**
 * Ejecucion de la suite completa de pruebas
 */
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_${PACKAGE_NAME}() {
      let suite = get_test_cases();

      for (input, expected) in suite {
        // assert_eq!(
        //   Solution::${PACKAGE_NAME}(/* input */),
        //   expected,
        //   "{}",
        //   format!("{:?}", input).red().italic().underline()
        // );
      }
    }
}
EOF

    echo "⚔️  Trial $NUMBER is ready for training in: $BIN_FILE"
  fi
  ;;

-t | --train)
  BIN_NAME=$(find "$BIN_DIR" -maxdepth 1 -name "${VALUE}_*.rs" | head -1 | xargs basename 2>/dev/null | sed 's/\.rs$//')
  if [ -n "$BIN_NAME" ]; then
    echo "🌌 Initiating Trial ${VALUE}..."
    cargo test --manifest-path "${DIRECTORY}/Cargo.toml" --bin "$BIN_NAME"
  else
    echo "❌ Error: Trial '${VALUE}' does not exist."
  fi
  ;;

-r | --run)
  CASE_INDEX=$3
  BIN_NAME=$(find "$BIN_DIR" -maxdepth 1 -name "${VALUE}_*.rs" | head -1 | xargs basename 2>/dev/null | sed 's/\.rs$//')
  if [ -n "$BIN_NAME" ]; then
    if [ -n "$CASE_INDEX" ]; then
      echo "🚀 Running Trial ${VALUE} (case #${CASE_INDEX})..."
      TRIAL_CASE="$CASE_INDEX" cargo run --quiet --manifest-path "${DIRECTORY}/Cargo.toml" --bin "$BIN_NAME"
    else
      echo "🚀 Running Trial ${VALUE}..."
      cargo run --quiet --manifest-path "${DIRECTORY}/Cargo.toml" --bin "$BIN_NAME"
    fi
  else
    echo "❌ Error: Trial '${VALUE}' does not exist."
  fi
  ;;

-l | --log)
  echo "📜 Trial Log — Jedi Academy:"
  echo "-----------------------------"
  for bin_file in "$BIN_DIR"/*.rs; do
    [ -f "$bin_file" ] && printf "  %s\n" "$(basename "$bin_file" .rs)"
  done
  ;;

*)
  show_help
  ;;
esac
