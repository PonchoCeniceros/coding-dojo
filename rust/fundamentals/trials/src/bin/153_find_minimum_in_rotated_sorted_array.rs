use colored::*;

struct Solution;

/**
 * Solución a implementar
 */
impl Solution {
    fn get_delta(nums: &[i32]) -> usize {
        let mut l: i32 = 0;
        let mut r = nums.len() as i32 - 1;

        while l <= r {
            if nums[l as usize] == nums[r as usize] {
                return l as usize;
            }

            let m = l + (r - l) / 2;
            let mi = m as usize;

            if nums[mi] < nums[r as usize] {
                if nums[mi] < nums[mi.saturating_sub(1)] {
                    return mi;
                } else {
                    r = m - 1 // linea original
                }
            } else {
                l = m + 1
            }
        }

        l as usize
    }

    pub fn find_min(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }

        if nums[0] < nums[nums.len() - 1] {
            nums[0]
        } else {
            let delta = Solution::get_delta(&nums);
            nums[delta..nums.len()][0]
        }
    }
}

/**
 * Casos de prueba
 *
 * casos borde:
 * E1. arr rotado
 * E2. arr no rotado
 * E3. arr de longitud 1
 * E4. arr rotado arr.len veces (igual que no rotado)
 */
fn get_test_cases() -> Vec<(Vec<i32>, i32)> {
    vec![
        /*0*/ (vec![3, 4, 5, 1, 2], 1), // E1
        /*1*/ (vec![4, 5, 6, 7, 0, 1, 2], 0), // E1
        /*2*/ (vec![11, 13, 15, 17], 11), // E2
        /*2*/ (vec![7], 7), // E3
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
