library(pracma)

# 输入矩阵A
A = matrix(c(-1,1,0,0,0,0,0,1,-1,-1,0,0,0,1,-1,0,1,0,-1,0), nrow=4, byrow=TRUE)

# 计算零空间基
N = nullspace(A)
if (is.null(N)) {
  stop("零空间仅包含零向量")
}

# 筛选极射线
extreme_rays = list()
for (i in 1:ncol(N)) {
  x = N[, i]
  # 检查约束有效性（假设Ax=0）
  active = sum(abs(A %*% x) < 1e-10)
  if (active >= nrow(A) - 1) {
    extreme_rays[[length(extreme_rays) + 1]] = x
  }
}

# 定义归一化函数：将第一个元素设为1,并过滤首元素为0的向量
normalize_first_element <- function(v) {
  if (abs(v[1]) < 1e-10) {
    return(NULL)  # 首元素为0的向量被过滤
  } else {
    scaled <- v / v[1]          # 缩放首元素为1
    scaled_rounded <- round(scaled, 6)  # 六位小数舍入
    return(scaled_rounded)
  }
}

# 应用归一化并去重
scaled_rays <- lapply(extreme_rays, normalize_first_element)
scaled_rays <- scaled_rays[!sapply(scaled_rays, is.null)]  # 删除NULL
unique_rays <- unique(scaled_rays)  # 去重

# 输出结果
if (length(unique_rays) == 0) {
  cat("警告：所有极射线首元素为0,无法标准化为1\n")
} else {
  cat("标准化后的极射线（首元素=1）：\n")
  print(do.call(rbind, unique_rays))
}
