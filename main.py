def kbig2(nums, k):
	t = []
	t= nums.copy()
	for i in range(k):
		m = max(t)
		t.pop(t.index(m))
	return m