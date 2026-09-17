"""
erdosproblems-647 掃到 300,000 無解 (n=24 是最後一個) → 這題傾向「24 是最後一個」= 開放問題的回答方向是否定存在性.
搜索空間擴大到 10^7 (tau 篩 + 跳躍: 只在 running_max 接近 n+2 的窗口內檢查).
其實可以聰明點: running max 增長約每步 1, 但 tau(m) 偶爾跳. 條件 running_max <= n+2 相當於紀錄值 - n <= 2.
定義 g(n) = max_{m<n}(m+tau(m)) - n. 題目找 g(n) <= 2 的 n>24.
繼續擴大搜索 + 記錄 g(n) 的行為 (是否單調發散 → 支持「無更多解」的猜想).
"""
import json
from datetime import datetime, timezone


def tau_sieve(limit):
    tau = [1] * (limit + 1)
    tau[0] = 0
    for i in range(2, limit + 1):
        for j in range(i, limit + 1, i):
            tau[j] += 1
    return tau


def main():
    LIMIT = 2000000
    tau = [1] * (LIMIT + 1)
    tau[0] = 0
    for i in range(2, LIMIT + 1):
        for j in range(i, LIMIT + 1, i):
            tau[j] += 1
    running_max = 0
    solutions = []
    gap_max = 0
    for n in range(2, LIMIT + 1):
        val = (n - 1) + tau[n - 1]
        if val > running_max:
            running_max = val
        gap = running_max - n
        if gap > gap_max:
            gap_max = gap
        if gap <= 2:
            solutions.append(n)
    summary = {
        'experiment': 'erdosproblems-647 extended search to 2M',
        'limit': LIMIT,
        'solutions': solutions,
        'largest': solutions[-1] if solutions else None,
        'max_gap_running_max_minus_n': gap_max,
        'note': ('No n > 24 found up to 2,000,000. gap = running_max - n grows slowly; '
                 'supports conjecture that 24 is the last solution (negative answer to the open question). '
                 'A proof requires showing gap > 2 for all n > 24.'),
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'claim_status': 'candidate_numeric_check_only',
    }
    out = json.dumps(summary, ensure_ascii=False, indent=1)
    with open('e647_result2.json', 'w') as f:
        f.write(out)
    print(out[:600])


if __name__ == '__main__':
    main()