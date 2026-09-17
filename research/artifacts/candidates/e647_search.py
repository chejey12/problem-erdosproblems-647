"""
erdosproblems-647 ($500, active): tau(m) 問題.
題目: 是否存在 n>24 使得 max_{m<n}(m+tau(m)) <= n+2?
即: n 之前的所有 m, m+tau(m) 都不超過 n+2. 換言之 n+2 是前 n 項的紀錄高度.
這是可完全計算的問題! 窮舉 n 到很大範圍找滿足條件的 n.
m+tau(m): tau 計算用因數分解. 窮舉 n 至 10^7 或更高.
注意 m < n 的條件, max over m in [1, n-1].
"""
import json
import math
from datetime import datetime, timezone


def tau_sieve(limit: int):
    """tau(1..limit) 用篩法."""
    tau = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            tau[j] += 1
    return tau


def main():
    LIMIT = 300000
    tau = tau_sieve(LIMIT)
    # max_{m<n}(m+tau(m))
    running_max = 0
    answers = []
    for n in range(2, LIMIT + 1):
        m = n - 1
        val = m + tau[m]
        if val > running_max:
            running_max = val
        # 條件: max_{m<n}(m+tau(m)) <= n+2
        if running_max <= n + 2:
            answers.append(n)
    summary = {
        'experiment': 'erdosproblems-647 exhaustive search',
        'limit': LIMIT,
        'known_answer': 24,
        'solutions_found': answers[:50],
        'num_solutions': len(answers),
        'largest_solution': answers[-1] if answers else None,
        'note': ('Condition: running max of m+tau(m) for m<n stays <= n+2. Known n=24 works. '
                 'Search extends to LIMIT; finding n>24 answers the question affirmatively.'),
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'claim_status': 'candidate_numeric_check_only',
    }
    out = json.dumps(summary, ensure_ascii=False, indent=1)
    with open('e647_result.json', 'w') as f:
        f.write(out)
    print(out[:700])


if __name__ == '__main__':
    main()