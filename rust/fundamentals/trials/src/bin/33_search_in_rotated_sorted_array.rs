use colored::*;

struct Solution;

/**
 * Implement your solution here
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

    fn make_bs(nums: &[i32], target: i32, delta: i32) -> i32 {
        let mut l = 0;
        let mut r = nums.len() as i32 - 1;

        while l <= r {
            let m = l + (r - l) / 2;

            if target == nums[m as usize] {
                return m + delta;
            }

            if target < nums[m as usize] {
                r = m - 1;
            }

            if target > nums[m as usize] {
                l = m + 1;
            }
        }

        -1
    }

    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        // #1 primero encontrar el cero (el desplazamiento)
        let delta = Solution::get_delta(&nums);
        println!("δ = {}", delta);

        if delta == 0 {
            if nums[0] < nums[nums.len() - 1] {
                return Solution::make_bs(&nums, target, 0_i32);
            } else {
                let nums_izq = &nums[0..1];
                let nums_der = &nums[1..nums.len()];

                return if nums[0] == target {
                    Solution::make_bs(nums_izq, target, 0_i32)
                } else {
                    Solution::make_bs(nums_der, target, nums_izq.len() as i32)
                };
            }
        };

        // #2 luego hacer la BS considerando el desplazamiento
        let l = 0_i32;
        let s = delta;
        let t = delta;
        let r = nums.len() as i32;

        let nums_izq = &nums[(l as usize)..s];
        let nums_der = &nums[t..r as usize];

        // nums[l as usize] <= target && target <= nums[s],
        // nums[t] <= target && target <= nums[(r - 1) as usize]

        if nums[l as usize] <= target && target <= nums[s.saturating_sub(1)] {
            // println!("slice izquierdo");
            // slice izquierdo
            Solution::make_bs(nums_izq, target, 0_i32)
        } else {
            // println!("slice derecho");
            // slice derecho
            Solution::make_bs(nums_der, target, nums_izq.len() as i32)
        }
    }
}

fn get_test_cases() -> Vec<((Vec<i32>, i32), i32)> {
    vec![
        /*0*/ ((vec![5, 1, 3], 5), 0),
        /*1*/ ((vec![3, 5, 1], 3), 0),
        /*2*/ ((vec![3, 1], 3), 0),
        /*3*/ ((vec![1, 3], 3), 1),
        /*4*/ ((vec![6, 7, 0, 1, 2, 4, 5], 0), 2),
        /*5*/ ((vec![4, 5, 6, 7, 0, 1, 2], 0), 4),
        /*6*/ ((vec![4, 5, 6, 7, 0, 1, 2], 3), -1),
        /*7*/ ((vec![1], 0), -1),
        /*8*/ ((vec![4, 5, 6, 7, 8, 1, 2, 3], 8), 4),
    ]
}

fn main() {
    const DEFAULT: usize = 5;
    let cases = get_test_cases();

    let idx: usize = std::env::var("TRIAL_CASE")
        .ok()
        .and_then(|v| v.parse().ok())
        .unwrap_or(DEFAULT);

    let (input, expected) = &cases[idx];
    let ans = Solution::search(input.0.clone(), input.1);
    println!(
        "{}:{}",
        format!("{}", ans).green().italic().underline(),
        format!("{}", expected).blue().italic().underline()
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_search_in_rotated_sorted_array() {
        let cases = get_test_cases();

        for (input, expected) in cases {
            assert_eq!(
                Solution::search(input.0.clone(), input.1),
                expected,
                "{}",
                format!("{:?}", input).red().italic().underline()
            );
        }
    }
}
