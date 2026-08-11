use colored::*;

struct Solution;

/**
 * Solución a implementar
 */
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        println!("{:?}", nums);
        0
    }
}

/**
 * Casos de prueba
 */
fn get_test_cases() -> Vec<(Vec<i32>, i32)> {
    vec![
        /*0*/ (vec![3, 4, 5, 1, 2], 1),
        /*1*/ (vec![4, 5, 6, 7, 0, 1, 2], 0),
        /*2*/ (vec![11, 13, 15, 17], 11),
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
    let answer = Solution::find_min(input.clone());
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
    fn test_find_minimum_in_rotated_sorted_array() {
        let suite = get_test_cases();

        for (input, expected) in suite {
            assert_eq!(
                Solution::find_min(input.clone()),
                expected,
                "{}",
                format!("{:?}", input).red().italic().underline()
            );
        }
    }
}
