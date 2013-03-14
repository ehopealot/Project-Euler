
$cache = {}
def partition(k, n)
  return 0 if k > n
  return 1 if n == k
  return $cache[[k, n]] if $cache[[k, n]]
  $cache[[k, n]] = partition(k+1, n) + partition(k, n-k)
end


partition(1, 100)

p $cache[[1, 100]] - 1
   