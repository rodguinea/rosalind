def prob_dominant(k, m, n):
    p_kk = k / (k + m + n) * (k - 1) / (k - 1 + m + n)
    p_km = k / (k + m + n) * m / (k - 1 + m + n)
    p_kn = k / (k + m + n) * n / (k - 1 + m + n)

    p_mk = m / (k + m + n) * k / (k + m - 1 + n)
    p_mm = m / (k + m + n) * (m - 1) / (k + m - 1 + n) * 0.75
    p_mn = m / (k + m + n) * n / (k + m - 1 + n) * 0.50

    p_nk = n / (k + m + n) * k / (k + m + n - 1)
    p_nm = n / (k + m + n) * m / (k + m + n - 1) * 0.50

    total_prob = p_kk + p_km + p_kn + p_mk + p_mm + p_mn + p_nk + p_nm
    return total_prob
