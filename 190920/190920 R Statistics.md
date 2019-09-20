# 190920 R Statistics

## REVIEW

단일 집단을 대상으로 전, 후에 대해 표본 추출해서 비율의 차이 비교  검정 - binom.test() (유의순준과 유의확률)
단일 집단의 평균과 어떤 특정한 집단의 평균의 차이를 검정하기 위해서 단일 집단의 평균이 정규분포를 이루는지 먼저 검정 -shapiro.test()
단일 집단의 평균이 정규분포를 따르는 경우 t.test() (유의확률과 t검정통계량)
단일 집단을 평균이 정규분포를 따르지 않는 경우 wilcox.text()



두집단을 대상으로 비율 검정 (독립표본 이항분포 비율 검정) - prop.test()
두집단을 대상으로 평균 검정 ->  두 집단의 평균의 정규분포가 동일한지 검정 (동질성 검정 -var.test() )
두 집단의 평균이 정규분포를 따르는 경우 t.test()
두 집단의 평균이 정규분포를 따르지 않는 경우 wilcox.text()



대응 두 집단 (예] 교수법 전, 교수법 후 동일 대상의 서로 다른 점수)의 평균 차이 비교
대응 두 집단의 평균의 정규분포가 동일한지 검정 (동질성 검정 -var.test() )
대응 두 집단의 평균이 정규분포를 따르는 경우 t.test()
대응 두 집단의 평균이 정규분포를 따르지 않는 경우 wilcox.text()



세 집단 대상으로 비율 검정 - prop.test()
세 집단 대상으로 평균 검정 - 분산분석, F검정
세 집단의 평균의 정규분포가 동일한지 검정 (동질성 검정 - bartlett.test())
세 집단의 평균이 정규분포를 따르는 경우 aov()
세 집단의 정규분포를 따르지 않는 경우 kruskal.test()
사후 검정 TukeyHSD()



요인 분석 - 다수의 변수를 대상으로 변수간의 관계를 분석하여 결과를 이용하여 상관분석이나 회귀분석의 설명변수(독립변수)로 활용하기 위해 수행하는 분석

변수의 주요 성분 분석 요인수를 알아보려면
1. 주성분 분석 - prcomp()
2. 고유값(변수의 상관계수 행렬)으로 요인수 분석 - eigen()

변수들간의 상관관계 분석으로 요인 분석 - 변수들간의 상관성을 이용해서 공통요인 추출 factanal(dataset, factors="" , rotation="", scores="") 

-------

## I. 기술통계분석

### 1. 요인분석

#### 1) 요인점수를 이용한 요인 적재량 시각화

```R
> s1 <- c(1, 2, 1, 2, 3, 4, 2, 3, 4, 5)
> s2 <- c(1, 3, 1, 2, 3, 4, 2, 4, 3, 4)
> s3 <- c(2, 3, 2, 3, 2, 3, 5, 3, 4, 2)
> s4 <- c(2, 4, 2, 3, 2, 3, 5, 3, 4, 1)
> s5 <- c(4, 5, 4, 5, 2, 1, 5, 2, 4, 3)
> s6 <- c(4, 3, 4, 4, 2, 1, 5, 2, 4, 2)
> name <-1:10 
> subject <- data.frame(s1, s2, s3, s4, s5, s6)


> str(subject)
'data.frame':	10 obs. of  6 variables:
 $ s1: num  1 2 1 2 3 4 2 3 4 5
 $ s2: num  1 3 1 2 3 4 2 4 3 4
 $ s3: num  2 3 2 3 2 3 5 3 4 2
 $ s4: num  2 4 2 3 2 3 5 3 4 1
 $ s5: num  4 5 4 5 2 1 5 2 4 3
 $ s6: num  4 3 4 4 2 1 5 2 4 2


> result <- factanal(subject, factors=2, rotation="varimax")
> result
Call:
factanal(x = subject, factors = 2, rotation = "varimax")

Uniquenesses:
   s1    s2    s3    s4    s5    s6 
0.250 0.015 0.005 0.136 0.407 0.107 

Loadings:
   Factor1 Factor2
s1  0.862         
s2  0.988         
s3          0.997 
s4 -0.115   0.923 
s5 -0.692   0.338 
s6 -0.846   0.421 

               Factor1 Factor2
SS loadings      2.928   2.152
Proportion Var   0.488   0.359
Cumulative Var   0.488   0.847

Test of the hypothesis that 2 factors are sufficient.
The chi square statistic is 11.32 on 4 degrees of freedom.
The p-value is 0.0232 


> result <- factanal(subject, factors=3, rotation="varimax" , scores="regression")
> result
Call:
factanal(x = subject, factors = 3, scores = "regression", rotation = "varimax")
Uniquenesses:
   s1    s2    s3    s4    s5    s6 
0.005 0.056 0.051 0.005 0.240 0.005 

Loadings:
   Factor1 Factor2 Factor3
s1 -0.379           0.923 
s2 -0.710   0.140   0.649 
s3  0.236   0.931   0.166 
s4  0.120   0.983  -0.118 
s5  0.771   0.297  -0.278 
s6  0.900   0.301  -0.307 

               Factor1 Factor2 Factor3
SS loadings      2.122   2.031   1.486
Proportion Var   0.354   0.339   0.248
Cumulative Var   0.354   0.692   0.940

The degrees of freedom for the model is 0 and the fit was 0.7745

# 요인점수 시각화
# 요인점수 플롯그래프 생성하고 라벨 붙이기
> plot(result$scores[, c(1:2)], main="Factor1과 Factor2의 요인점수 행렬")
> text(result$scores[, 1], result$scores[, 2], labels=name, cex=0.7, pos=3, col="red")

# 그 위에 적재량 추가하고 라벨 붙이기
> points(result$loadings[, c(1:2)], pch=19, col="blue")
> text(result$loadings[, 1], result$loadings[, 2], labels=rownames(result$loadings),       cex=0.8, pos=3, col="green")
```

![1](190920%20R%20Statistics.assets/1.JPG)

- scatterplot3d 활용해서 시각화해보기

```R
install.packages("scatterplot3d")
library(scatterplot3d)

# 요인점수별 분류
Factor1 <- result$scores[, 1]
Factor2 <- result$scores[, 2]
Factor3 <- result$scores[, 3]

# scatterplot3d(밑변, 오른쪽 변, 왼쪽 변, type)
> d3 <- scatterplot3d(Factor1, Factor2, Factor3, type='p')

# 요인적재량 표시
> Loadings1 <- result$loadings[, 1]
> Loadings2 <- result$loadings[, 2]
> Loadings3 <- result$loadings[, 3]
> d3$points3d(Loadings1, Loadings2, Loadings3, bg="red", pch=21, cex=2, type="h")
```

![2](190920%20R%20Statistics.assets/2.JPG)



#### 2) 요인별 변수 묶기

- 요인분석을 통해서 각 요인에 속하는 입력변수들을 묶어서 파생변수를 생성할 수 있는데 이러한 파생변수는 상관분석이나 회귀분석에서 독립변수로 사용할 수 있다. 

- 파생 변수는 가독성과 설득력이 가장 높은 산술평균 방식을 적용하여 생성할 수 있다.
  - 단계1 ] 요인별 파생변수를 대상으로 데이터프레임 생성

  - 단계2 ] 요인별 산술평균 계산
  - 단계3 ] 상관관계 분석

```R
#요인 분석 결과를 이용하여  변수 묶기->상관분석이나 회귀분석에서 독립변수로 사용할 수 있는 파생변수 생성

# Factor1은 응용과학
# Factor2는 응용수학
# Factor3은 자연과학

# 요인별 데이터프레임 생성
> app <- data.frame(subject$s5, subject$s6)
> soc <- data.frame(subject$s3, subject$s4)
> nat <- data.frame(subject$s1, subject$s2)

# 요인별 산술평균 계산해 파생변수 생성
> app_science <- round((app$subject.s5 + app$subject.s6)/ncol(app), 2)
> soc_science <- round((soc$subject.s3 + soc$subject.s4)/ncol(soc), 2)
> nat_science <- round((nat$subject.s1 + nat$subject.s2)/ncol(nat), 2)

# 세 개의 요인에 대해 상관관계 분석
> subject_factor_df <- data.frame(app_science, soc_science, nat_science)
> cor(subject_factor_df)
            app_science soc_science nat_science
app_science   1.0000000  0.43572654 -0.68903024
soc_science   0.4357265  1.00000000 -0.02570212
nat_science  -0.6890302 -0.02570212  1.00000000
# 참고 : -1 < 상관계수 < -0.7 : 강한 음의 선형관계 /-0.7 < 상관계수 < -0.3 : 뚜렷한 음의 선형 관계 / -0.3 < 상관계수 < -0.1 : 약한 음의 선형 관계 / -0.1 < 상관계수 < 0.1 : 무시될 수 있음 / 0.1 < 상관계수 < 0.3 :  약한 양의 선형 관계 / 0.3 < 상관계수 < 0.7 : 뚜렷한 양의 선형 관계 / 0.7 < 상관계수 < 1.0 : 강한 양의 선형 관계
# 해석 : 응용과학과 사회과학은 약간의 양의 상관성을 나타내고, 응용과학과 자연과학은 약간의 음의 상관성을 나타내며, 사회과학과 자연과학은 상관성이 없음을 나타낸다.
```



#### 3) 잘못 분류된 요인 제거로 변수 정제 실습

- 요인분석을 위해서 spss 에서 사용되는 데이터를 R로 가져오기 위해서 memisc 패키지를 설치하고, 패키지에서 제공되는 spss.system.file() 함수를 이용하여 데이터를 가져온 후 데이터프레임으로 변경하여 요인분석을 위한 데이터를 준비한다

```R
# 음료수 제품의 11개의 변수 (친밀도, 적절성, 만족도 3가지 영역)
# 특정 변수가 묶일 것으로 예상되는 요인드이 묶이지 않는 경우, 해당 변수를 제거하는 정제작업이 필요하다.

> install.packages("memisc")
> library(memisc)

> data.spss <- as.data.set(spss.system.file("./data/drinking_water.sav"))
> str(data.spss)
Data set with 380 obs. of 15 variables:
 $ q1  : Itvl. item  num  3 3 3 3 3 1 2 2 2 4 ...
 $ q2  : Itvl. item  num  2 3 3 3 3 1 2 2 2 3 ...
 $ q3  : Itvl. item  num  3 3 3 3 2 1 2 1 1 3 ...
 $ q4  : Itvl. item  num  3 3 4 1 2 1 3 2 2 3 ...
 $ q5  : Itvl. item  num  4 3 3 3 3 1 2 1 3 4 ...
 $ q6  : Itvl. item  num  3 3 4 2 3 1 3 2 3 3 ...
 $ q7  : Itvl. item  num  4 2 3 3 2 1 5 1 1 3 ...
 $ q8  : Itvl. item  num  3 3 4 2 2 3 4 2 3 4 ...
 $ q9  : Itvl. item  num  4 3 4 2 2 3 4 2 2 2 ...
 $ q10 : Itvl. item  num  3 2 4 2 2 3 4 2 3 3 ...
 $ q11 : Itvl. item  num  4 3 4 2 2 3 4 2 1 4 ...
 $ 성별: Nmnl. item w/ 2 labels for 1,...  num  1 2 1 2 2 1 2 2 2 2 ...
 $ 연령: Nmnl. item w/ 6 labels for 1,...  num  2 2 2 2 2 3 2 2 2 2 ...
 $ 지역: Nmnl. item w/ 5 labels for 1,...  num  1 1 1 1 1 1 1 1 1 1 ...
 $ 학력: Nmnl. item w/ 5 labels for 1,...  num  3 3 2 3 3 3 4 3 4 5 ...

# 제품 친밀도(q1:브랜드, q2:친근감, q3:익숙함, q4:편안함)
# 제품 적절성(q5:가격적절성, q6:당도적절성, q7:성분적절성)
# 제품 만족도(q8:음료의 목넘김, q9:맛, q10:향 ,q11:가격)

# 데이터프레임으로 변환해 저장
> drinking_water <- data.spss[1:11]
> drinking_water_df <- as.data.frame(data.spss[1:11])

# 요인분석 (factanal 사용)
> result <- factanal(drinking_water_df, factors=3, rotation="varimax")
> result

Call:
factanal(x = drinking_water_df, factors = 3, rotation = "varimax")
# Uniqueness는 모든 변수에 대해서 0.5를 기준으로 이하의 값이면 유효하다, 그렇지 않으면 유효하지 않다고 분석 할 수 있는 기준
Uniquenesses:
   q1    q2    q3    q4    q5    q6    q7    q8    q9   q10   q11 
0.321 0.238 0.284 0.447 0.425 0.373 0.403 0.375 0.199 0.227 0.409 

Loadings:
    Factor1 Factor2 Factor3
q1  0.201   0.762   0.240  
q2  0.172   0.813   0.266  
q3  0.141   0.762   0.340  
q4  0.250   0.281   0.641  
q5  0.162   0.488   0.557  
q6  0.224   0.312   0.693  
q7  0.235   0.219   0.703  
q8  0.695   0.225   0.304  
q9  0.873   0.122   0.155  
q10 0.852   0.144   0.161  
q11 0.719   0.152   0.225  

               Factor1 Factor2 Factor3
SS loadings      2.772   2.394   2.133
Proportion Var   0.252   0.218   0.194
Cumulative Var   0.252   0.470   0.664

Test of the hypothesis that 3 factors are sufficient.
The chi square statistic is 40.57 on 25 degrees of freedom.
The p-value is 0.0255 
# 적재량에 있어서 Factor1은 q8~q11, Factor2는 q1~q3, Factor3은 q4~q7까지 상관도가 높다. 그런데 q4만 지금 Factor2에 안 끼고 Factor3에 껴버렸음
# 유의확률이 0.0255로 유의수준 0.05보다 낮으므로 요인수 선택에 문제가 있다고 볼 수 있다. (여기서의 p-value는 카이 제곱 검정의 결과로서 기대치와 관찰치에 차이가 있음을 알려주는 확률값)


> dw_df <- drinking_water_df[-4]
> str(dw_df)
'data.frame':	380 obs. of  10 variables:
 $ q1 : num  3 3 3 3 3 1 2 2 2 4 ...
 $ q2 : num  2 3 3 3 3 1 2 2 2 3 ...
 $ q3 : num  3 3 3 3 2 1 2 1 1 3 ...
 $ q5 : num  4 3 3 3 3 1 2 1 3 4 ...
 $ q6 : num  3 3 4 2 3 1 3 2 3 3 ...
 $ q7 : num  4 2 3 3 2 1 5 1 1 3 ...
 $ q8 : num  3 3 4 2 2 3 4 2 3 4 ...
 $ q9 : num  4 3 4 2 2 3 4 2 2 2 ...
 $ q10: num  3 2 4 2 2 3 4 2 3 3 ...
 $ q11: num  4 3 4 2 2 3 4 2 1 4 ...


# 요인별 변수 묶기
> s <- data.frame(dw_df$q8, dw_df$q9, dw_df$q10, dw_df$q11) # 만족도
> c <- data.frame(dw_df$q1, dw_df$q2, dw_df$q3) # 친밀도
> p <- data.frame(dw_df$q5, dw_df$q6, dw_df$q7) # 적절성


# 요인별 산술평균 계산
> satisfaction <- round((dw_df$q8 + dw_df$q9 + dw_df$q10 + dw_df$q11)/ncol(s), 2)
> closeness <- round((dw_df$q1 + dw_df$q2 + dw_df$q3)/ncol(c), 2)
> pertinence <- round((dw_df$q5 + dw_df$q6 + dw_df$q7)/ncol(p), 2)


# 상관관계 분석
> dwf_df <- data.frame(satisfaction, closeness, pertinence)
> colnames(dwf_df) <-c("제품 만족도", "제품 친밀도", "제품 적절성")
> cor(dwf_df)
            제품 만족도 제품 친밀도 제품 적절성
제품 만족도   1.0000000   0.4047543   0.4825335
제품 친밀도   0.4047543   1.0000000   0.6344751
제품 적절성   0.4825335   0.6344751   1.0000000
# 해석 : 제품 만족도와 제품 친밀도는 약간 양의 상관관계를, 제품 만족도와 제품 적절성은 그것보단 조금 강한 양의 상관관계를, 제품 친밀도와 제품 적절성은 높은 상관관계를 가진다. => 높은 상관관계를 가진 변수들을 설명 변수로 사용할 수 있을 것!
```



### 2. 상관관계 분석

- 변수 간의 관련성을 분석하기 위해 사용하는 분석방법

- 하나의 변수가 다른 변수와 관련성이 있는지, 있다면 어느 정도의 관련성이 있는지를 개관할 수 있는 분석기법
  - 예)  브랜드 인지도의 관련성광고비와 매출액 사이의 관련성 등을 분석하는데 이용한다

- 상관관계 분석(Correlation Analysis) 중요사항

  - 회귀분석에서 변수 간의 인과관계를 분석하기 전에 변수 간의 관련성을 분석하는 선행자료(가설 검정 전 수행)로 이용한다.

  - 변수 간의 관련성은 상관계수인 피어슨(Pearson) R 계수를 이용해 관련성의 유무와 정도를 파악한다.

  - 상관관계 분석의 척도인 피어슨 상관계수 R과 상관관계 정도

| 피어슨 상관계수 R |    상관관계 정도     |
| :---------------: | :------------------: |
|     ±0.9이상      |  매우 높은 상관관계  |
|    ±0.9 ~ ±0.7    |   높은   상관관계    |
|    ±0.7 ~±0.4     | 다소   높은 상관관계 |
|    ±0.4 ~ ±0.2    |    낮은 상관관계     |
|     ±0.2 미만     |    상관관계 없음     |

- 상관계수  
  - 두 변량 X, Y 사이의 상관관계의 정도를 나타내는 수치(계수)이다.

  - -1과 1사이의 값을 가지며, 절대값이 1에 가까울수록 두 변량 간의 상관관계의 정도가 높은 것으로 볼 수 있다.

  - 상관계수로 두 변량의 인과관계는 알 수 없다. 

  - 상관계수로 두 변량의 선형 관계만 파악할 수 있다

- 상관계수 r과 상관관계 정도
  - 완전 정(+) 상관관계는 X의 갓이 증가하면 Y의 값도 증가하는 형태로 r=1이며, 완전 부(-) 상관관계는 x의 값이 증가하면 y의 값은 감소하는 형태로 r=-1이다.

![1568944103475](190920%20R%20Statistics.assets/1568944103475.png)

- 상관계수 보기  

  - 변수 간의 상관계수는 stats 패키지에서 제공되는 cor() 함수를 이용

  ```R
  cor( x, y=NULL, use=“everything”, method=c(“pearson”, “kendall”, “spearman”))
  ```

  - corrgram() 은 상관계수와 상관계수에 따라서 색의 농도로 시각화해 준다.
  - 서열척도로 구성된 변수에 대해서 상관계수를 구하기 위해서는 spearman을 적용할 수 있다.

  - 대상 변수가 등간척도 또는 비율척도일 때 피어슨(Pearson) 상관계수를 적용할 수 있다

- 상관관계 분석의 유형  

  - 단순 상관 관계 
  - 다중 상관 관계 – 둘 이상의 변수들이 어느 한 변수와 관계를 갖는 경우 그 정도를 파악

  - 편(Partial) 상관관계 
  - 부분(Semi partial) 상관 관계



#### 1) 상관분석(correlation Analysis)

- 데이터 내의 두 변수간의 관계를 알아보기 위한 분석 방법

- 상관계수(Correlation coefficient)를 이용

- 상관분석은 연속형, 순서형 자료를 대상으로 하고, 범주형은 불가능함

- 두 변수 간의 연관된 정도만 제시하고 있으며 회귀분석을 통해 두 변수 간 원인과 결과의 인과관계의 방향, 정도, 모형 적합을 통한 함수관계를 검토할 수 있음

- 두 변수의 상관성에 대한 예측이므로, 가설과 검증을 통해 통계적 유의성을 판단

- 등간성이나 비율성이 존재하지 않음

- 결정계수(R square)는 상관계수를 제공하여 나오는 값으로, 회귀분석에서 설명력을 의미



#### 2) 상관분석 절차

1) 변수들 간의 산점도 그리기

2) 산점도를 통해 직선관계를 파악

3) 상관계수 계산

4) 상관계수로 자료 해석

5) 상관관계의 유무, 정도에 따라 회귀분석 실시



#### 3) 상관분석 유형

- 피어슨 : 등간척도 이상으로 측정된 두 변수들의 상관계수 측정 방식
  - 연속성 변수, 정규성 가정
  - 대부분 많이 사용함
- 스피어만 : 서열척도인 두 변수들의 상관관계 측정 방식
  - 순서형 변수, 모수 방법
  - 순위를 기준으로 상관관계 측정
- 켄달 : 서열척도인 두 변수들의 상관관계 측정 방식
  - 순서형 변수, 비모수 방법



#### 4) 상관계수의 유의성 검정

- “상관계수는 0이다＂라는 귀무가설을 기각할 수 있는지 검정

- “유의 확률(양측검정) < 0.05인 경우 상관계수가 있다“ 고 할 수 있음



#### 5) 상관계수의 해석

- -1 < 상관계수 < -0.7 : 강한 음의 선형관계

- -0.7 < 상관계수 < -0.3 : 뚜렷한 음의 선형 관계

- -0.3 < 상관계수 < -0.1 : 약한 음의 선형 관계

- -0.1 < 상관계수 < 0.1 : 무시될 수 있음

- 0.1 < 상관계수 < 0.3 :  약한 양의 선형 관계

- 0.3 < 상관계수 < 0.7 : 뚜렷한 양의 선형 관계

- 0.7 < 상관계수 < 1.0 : 강한 양의 선형 관계



```R
#################### 상관관계분석 ####################
> result <- read.csv("./data/product.csv", header=TRUE)
> head(result)
  제품_친밀도 제품_적절성 제품_만족도
1           3           4           3
2           3           3           2
3           4           4           4
4           2           2           2
5           2           2           2
6           3           3           3

> str(result)
'data.frame':	264 obs. of  3 variables:
 $ 제품_친밀도: int  3 3 4 2 2 3 4 2 3 4 ...
 $ 제품_적절성: int  4 3 4 2 2 3 4 2 2 2 ...
 $ 제품_만족도: int  3 2 4 2 2 3 4 2 3 3 ...

> summary(result)
  제품_친밀도     제품_적절성     제품_만족도   
 Min.   :1.000   Min.   :1.000   Min.   :1.000  
 1st Qu.:2.000   1st Qu.:3.000   1st Qu.:3.000  
 Median :3.000   Median :3.000   Median :3.000  
 Mean   :2.928   Mean   :3.133   Mean   :3.095  
 3rd Qu.:4.000   3rd Qu.:4.000   3rd Qu.:4.000  
 Max.   :5.000   Max.   :5.000   Max.   :5.000

> sd(result$제품_친밀도); sd(result$제품_적절성); sd(result$제품_만족도);
[1] 0.9703446
[1] 0.8596574
[1] 0.8287436

> cor(result$제품_적절성, result$제품_만족도)
[1] 0.7668527

> cor(result$제품_만족도, result$제품_친밀도+result$제품_적절성)
[1] 0.7017394

> cor(result, method="pearson")
            제품_친밀도 제품_적절성 제품_만족도
제품_친밀도   1.0000000   0.4992086   0.4671450
제품_적절성   0.4992086   1.0000000   0.7668527
제품_만족도   0.4671450   0.7668527   1.0000000

> corrgram(result)
```

![3](190920%20R%20Statistics.assets/3.JPG)

```R
# 상관성, 밀도곡선, 유의확률 시각화
> install.packages("PerformanceAnalytics")
> library(PerformanceAnalytics)

# 상관성, p값(*), 정규분포 시각화
> chart.Correlation(result, histogram=, pch="+")
```

![4](190920%20R%20Statistics.assets/4.JPG)

### 3. 연습문제

```R
# 다음은 drinkig_water_example.sav 파일의 데이터 셋이 구성된 테이블이다. 전체 2개의 요인에 의해서 7개의 변수로 구성되어 있다. 아래에서 제시된 각 단계에 맞게 요인분석을 수행하시오.
# 요인 1001 (q1:브랜드, q2:친근감, q3: 익숙함)
# 제품 만족도 (q4:음료의 목넘김, q5:음료의 맛, q6:음료의 향 , q7:가격)


# 베리멕스 회전법, 요인수 2, 요인점수 회귀분석 방법을 적용하여 요인분석 하시오

# 요인적재량 행렬의 칼럼명 변경하시오 ("제품친밀도", "제품만족도")


# 요인점수를 이용한 요인적재량 시각화하시오

# 요인별 변수로 묶기

# 생성된 두 개의 요인을 데이터프레임으로 생성한 후 이를 이용하여 두 요인 간의 상관관계 계수를 제시하시오

```







## II. 예측분석 지도학습

### 1. 기계학습(Machine Learning)

- 알고리즘을 통해서 기계(컴퓨터, 로봇 등)에게 학습을 시킨 후 새로운 데이터가 들어오는 경우 해당 데이터의 결과를 예측하는 학문 분야

- 인간과 로봇과의 상호작용, 포털 사이트에서 검색어 자동 완성 기능, 악성 코드 탐지, 문자인식, 기계 오작동으로 인한 사고 발생 가능성 등을 예측하는 분야에서 이용된다.

- 데이터를 통해서 반복 학습으로 만들어진 모델을 바탕으로 최적의 판단이나 예측을 가능하게 해주는 것을 목표로 한다

- 기계학습 분류
  - 지도학습 – 사전에 입력과 출력에 대한 정보를 가지고 있는 상태에서 입력이 들어오는 경우 해당 출력이 나타나는 규칙을 발견(알고리즘 이용) 하고, 만들어진 모델(model)에 의해서 새로운 데이터를 추정 및 예측한다.

  - 비지도학습 – 최종적인 정보가 없는 상태에서 컴퓨터 스스로 공통점과 차이점 등의 패턴을 이용해서 규칙을 생성하고, 규칙을 통해서 분석 결과를 도출하는 방식
  - 비지도학습은 유사한 데이터를 그룹화해주는 군집화와 군집 내의 특성을 나태내는 연관분석 방법에 주로 이용된다 .
  - 지도학습과 비지도학습의 차이 비교
    - 지도학습은 영향을 미치는 독립변수와 영향을 받는 종속변수의 관계(x -> y)가 형성되지만, 비지도학습은 종속변수가 존재하지 않는다  

| 분류 |            지도학습             |           비지도학습            |
| :--: | :-----------------------------: | :-----------------------------: |
| 주관 |     사람의 개입에 의한 학습     |     컴퓨터에 의한 기계학습      |
| 기법 |    확률과 통계기반 추론통계     |   패턴분석 기반 데이터 마이닝   |
| 유형 | 회귀분석, 분류분석(y 변수 있음) | 군집분석, 연관분석(y 변수 없음) |
| 분야 |        인문. 사회   계열        |        공학. 자연   계열        |



#### 1) 혼돈 매트릭스(Confusion Matrix)

- 기계학습에 의해서 생성된 분류분석 모델의 성능을 지표화 할 수 있는 테이블로 모델에 의해서 예측한 값은 열(column)로 나타나고, 관측치의 값은 행(row)으로 표시된다.

|          |     예측치 P     |   예측치 N    |
| :------: | :--------------: | :-----------: |
| 관측치 P |  TP(참   긍정)   | 거짓 부정(FN) |
| 관측치 N | FP (거짓   긍정) |  참 부정(TN)  |

- 정분류율(Accuracy)  = (TP +TN) / 전체관측치(TN+FP+FN+TP)
   모델이 Yes로 판단한 것 중에서 실제로 Yes인 비율

- 분류율(Inaccuracy)  = (FN +FP) / 전체관측치(TN+FP+FN+TP) = 1- 정분류율

- 정확율(Precision)  = TP  / (TP +FP) 

- 재현율(Recall)  = TP  / (TP +FN) 
   관측치가 Yest인 것 중에서 모델이 Yes로 판단한 비율

- F1 점수(F1 score)  =(2 * (Precision * Recall) / (Precision + Recall)
  기계학습에서 Y변수가 갖는 1(Yes)과 0(No)의 비율이 불균형을 이루는 경우 모델의 평가결과로 F1 점수를 주로 이용한다.



#### 2) 지도 학습 절차  

- 단계 1] 학습데이터를 대상으로 알고리즘 (회귀, 분류 관련)적용

- 단계 2] 학습 후 모델 생성

- 단계 3] 검정데이터를 이용하여 생성된 모델의 정확도를 평가



#### 3) 회귀분석

- 특정변수(독립변수)가 다른 변수(종속변수)에  어떠한 영향을 미치는가를 분석하는 방법

- 인과관계가 있는지 등을 분석하기 위한 방법

- 한 변수의 값을 가지고 다른 변수의 값을 예측해 주는 분석 방법
- 회귀분석 (Regression Analysis)  중요사항
  - 가장 강력하고, 사용 범위가 넓은 분석 방법
  - 돌깁변수가 종속변수에 영향을 미치는 변수를 규명하고, 이들 변수에 의해서 회귀 방정식(Y=a+βX -> Y:종속변수, a:상수, β:회귀계수, X: 독립변수)을 도출하여 회귀선을 추정한다.
  - 회귀계수(β)는 단위시간에 따라 변하는 양(기울기)
  - 회귀선은 산점도에 위치한 각 점들의 정중앙을 통과하는 직선을 추정하는 최소제곱법을 이용
  - 독립변수와 종속변수가 모두 등간척도 또는 비율척도로 구성되어 있어야 한다.
- 회귀방정식의 이해  
  - 독립변수(X)와 종속변수(Y)에 대한 분포를 나타내는 산점도를 대상으로 최소자승의 원리를 적용하여 가장 적합한 선을 그릴 수 있다 (회귀선)
  - 회귀선은 두 집단의 분포에서 잔차(각 값들과 편차)들의 제곱의 합을 최소화시키는(최소제곱법) 회귀방정식에 의해서 만들어진다.

##### 1. 단순 회귀분석

> 독립변수와 종속변수가 각각 한 개일 경우 독립변수가 종속변수에 미치는 인과관계 등을 분석하고자 할 때 이용하는 분석 방법

- 회귀분석 (Regression Analysis)의 기본적인 가정 충족
  - 선형성 : 독립변수와 종속변수가 선형적이어야 한다. – 회귀선 확인

  - 잔차 정규성 : 잔차(오차)란 종속변수의 관측값과 회귀모델의 예측값 간의 차이로 잔차의 기대값은 0이며, 정규분포를 이루어야 한다 – 정규성 검정 확인
  - 잔차 독립성 : 잔차들은 서로 독립적이어야 한다. – 더빈 왓슨 값 확인
  - 잔차 등분산성 : 잔차들의 분산이 일정해야 한다 – 표준잔차와 표준예측치 도표
  - 다중 공산성 : 다중 회귀분석을 수행할 경우 3개 이상의 독립변수 간의 강한 상관관계로 인한 문제가 발생하지 않아야 한다. – 분산팽창요인(VIF) 확인

- 회귀분석 (Regression Analysis)의 분석 절차
  - 단계1] 회귀분석의 기본적인 가정이 충족되는지 확인한다. – 회귀분석의 기본적인 가정 충족 
  - 단계2] 분산분석의 F 값으로 회귀모형의 유의성 여부를 판단한다.
  - 단계3] 독립변수와 종속변수 간의 상관관계와 회귀모형의 설명력을 확인한다.
  - 단계4] 검정 통계량 t값에 대한 유의확률을 통해서 가설의 채택 여부를 결정한다.
  - 단계5] 회귀방정식을 적용하여 회귀식을 수립하고 결과를 해석한다.

- 회귀 방정식  Y=α + βX

  - α  : 절편,  β : 회귀계수, X: 독립 변수, Y: 종속변수

  - 절편(Intercept)는 x가 0일때 y값을 의미하고,
  - 기울기(gradient)는 x값의 변화에 따른 y 값의 변화하는 정도를 의미
  - fitted.values() – 모델의 적합값 확인
  - residuals() – 모델의 잔차 확인
  - 잔차와 적합값의 합으로 관측값을 계산 할 수 있다

- 회귀선(regression line)  
  - 두 변수 간의 예측관계에서 한 변수에 의해서 예측되는 다른 변수의 예측치들이  그 변수의 평균치로 회귀하는 경향이 있다고 하여 갈톤(Galton)에 의해서 명명됨
  - 한 변수의 증감이 다른 변수의 단위증가에 대해 어느 정도인가를 나타내는 선을 의미

- 회귀분석 결과는 요약 통계량을 구할 때 summary() 이용하여 확인할 수 있다.

- - 

```R
########### 회귀 분석 ###########
> product <- read.csv("./data/product.csv", header=TRUE)
> head(product)
  제품_친밀도 제품_적절성 제품_만족도
1           3           4           3
2           3           3           2
3           4           4           4
4           2           2           2
5           2           2           2
6           3           3           3
> str(product)
'data.frame':	264 obs. of  3 variables:
 $ 제품_친밀도: int  3 3 4 2 2 3 4 2 3 4 ...
 $ 제품_적절성: int  4 3 4 2 2 3 4 2 2 2 ...
 $ 제품_만족도: int  3 2 4 2 2 3 4 2 3 3 ...

> y<-product$제품_만족도  #종속변수
> x<-product$제품_적절성  #독립변수
> df <- data.frame(x, y)

# 단순 선형회귀 모델 생성 lm(y~x, data)
> library(stats)
> result.lm <- lm(formula=y~x, data=df)
> result.lm

Call:
lm(formula = y ~ x, data = df)

Coefficients:
(Intercept)            x  
     0.7789       0.7393 

# 생성된 선형회귀 모델의 적합값과 잔차 계산
> names(result.lm) # 모델 관련 정보확인
 [1] "coefficients"  "residuals"     "effects"       "rank"         
 [5] "fitted.values" "assign"        "qr"            "df.residual"  
 [9] "xlevels"       "call"          "terms"         "model" 

> fitted.values(result.lm)[1:2] # 모델의 적합값 확인
       1        2 
3.735963 2.996687 

> head(df, 1) # 관측값
  x y
1 4 3

> Y=0.7789+0.7393*4
> Y
[1] 3.7361

# 오차는 관측값-적합값
> 3-3.735963
[1] -0.735963 # 오차

> residuals(result.lm)[1:2]
         1          2
-0.7359630 -0.9966869

# 관측값은 잔차 + 적합값
> -0.7359630+3.735963
[1] 3

# 선형회귀분석 모델 시각화
> plot(formula=y~x, data=result)
> abline(result.lm, col="red") # 회귀선
```

![5](190920%20R%20Statistics.assets/5.JPG)

```R
#선형회귀분석 결과
> summary(result.lm)

Call:
lm(formula = y ~ x, data = df)

Residuals:
     Min       1Q   Median       3Q      Max 
-1.99669 -0.25741  0.00331  0.26404  1.26404 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.77886    0.12416   6.273 1.45e-09 ***
x            0.73928    0.03823  19.340  < 2e-16 ***
---
Signif. codes:  
0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.5329 on 262 degrees of freedom
Multiple R-squared:  0.5881,	Adjusted R-squared:  0.5865 
F-statistic:   374 on 1 and 262 DF,  p-value: < 2.2e-16

# Multiple R-squared: 0.5881 는 독립변수에 의해서 종속변수가 얼마만큼 설명되었는가(회귀모델의 설명력)
# Multiple R-squared 값은 독립변수와 종속변수 간의 상관관계를 나타내는 결정계수   
# 설명력이 1에 가까울수록 설명변수(독립변수)가 설명을 잘한다고 판단할 수 있다 => 변수의 모델링이 잘 되었다는 의미

#Adjusted R-squared:  0.5865은 오차를 감안하여 조정된 R 값으로 (실제 분석은 이 값을 적용한다.)

#F-statistic:   374 회귀모델의 적합성을 나타내며    
#p-value: < 2.2e-16 
#F-statistic와 p-value를 이용하여 회귀모델 자체를 신뢰할 수 있는지 판단
# p-value가 0.05보다 매우 작기 때문에 회귀선이 모델에 적합하다고 볼 수 있다.

# x            0.73928    0.03823  19.340  < 2e-16 ***
# x변수의 t=19.340 , p-value는 < 2e-16 이므로  p-value가 0.05보다 매우 작기 때문에 "제품의 가격과 품질을 결정하는 제품 적절성은 제품 만족도에 양의 영향을 미친다." 연구가설 채택
```



##### 2. 다중 회귀분석

- 여러 개의 독립변수가 동시에 한 개의 종속변수에 미치는 영향을 분석할 때 이용하는 분석방법

- 다수의 독립변수가 투입되기 때문에 한 독립변수가 다른 독립변수들에 의해서 설명되지 않은 부분을 의미하는 공차한계(Tolerance)와 공차한계의 역수로 표시되는 분산팽창요인(VIF)으로 다중 공선성에 문제가 없는지를 확인해야 한다
  - 다중공선성(Multicollinearity) 문제 
    - 한 독립변수의 값이 증가할 때 다른 독립변수의 값이 이와 관련하여 증가하거나 감소하는 현상
    - 대부분 다중회귀분석에서 독립변수들은 어느 정도 상관관계를 보이고 있기 때문에 다중 공선성은 존재하지만, 독립변수들이 강한 상관관계를 보이는 경우는 회귀분석의 결과를 신뢰하기가 어렵다.
    - 상관관계가 높은 독립변수 중 하나 혹은 일부를 제거하거나 변수를 변형시켜서 해결한다.
  - 분산 팽창요인 값을 확인하기 위해서 관련 패키지를 설치하고 vif() 함수를 이용하여 다중 공선성 문제를 확인한다

- 다중 공선성 문제 해결과 모델 성능 평가
  - 학습데이터와 검정데이터를 7:3 비율로 샘플링
  - 표본 추출
  - 다중 공선성 문제 해결 – 강한 상관관계를 갖는 독립변수를 제거하여 해결

  - 학습 데이터로부터 회귀모델 생성
  - 검정 통계량 분석하여 가설 검정

  - 검정 데이터를 이용하여 모델의 예측치 생성 – stats패키지의 predict() 
  - 회귀 모델 성능을 평가 – 상관계수를 이용 , 모델의 예측치(pred)와 검정데이터의 종속변수(y)를 이용하여 상관계수(r) 를 구하여 모델의 분류정확도를 평가한다

- 회귀분석은 선형성, 다중 공선성, 잔차의 정규성 등 몇 가지 기본 가정이 총족되어야 수행 할 수 있는 모두 검정 방법이다.

- 회귀 모델의 결과변수를 대상으로 잔차(오차) 분석과 다중 공선성 검사를 통해서 회귀분석의 기본 가정이 충족하는지 확인 실습

  - 잔차의 독립성 검정을 위해서 ‘lmtest’ 패키지의 dwtest() 의 인수로 회귀모델의 결과 변수를 적용하여 더빈 왓슨값을 확인

  - 더빈 왓슨값의 p-value가 0.05이상 (DW값 1~3범위)이면 잔차에 유의미한 자기 상관이 없다고 볼 수 있다.  즉 ‘독립성과 차이가 없다’
  - 독립변수(X)의 값에 대응하는 종속변수(Y)의 분산이 독립변수의 모든 값에 대해서 같다는 의미인 등분산성 검정을 위해서 회귀모델의 결과변수를 plot()함수의 인수로 적용하여 시각화를 통해서 등분산성 여부를 확인할 수 있다.
  - 잔차(Residudals) 0을 기준으로 적합값(Fitted values)의 분포가 좌우균등하면 잔차들은 ‘등분산성과 차이가 없다’라고 볼 수 있다.
  - 잔차의 정규성 검정을 위해서 회귀모델의 결과변수를 대상으로 잔차를 추출하고, shapiro.test() 함수를 이용하여 정규성을 검정

```R
############### 다중회귀분석 ################
# 연구가설(H1) : 제품의 적절성과 제품의 친밀도는 제품 만족도에 정(正)의 영향을 미친다.
# 귀무가설(H0) : 제품의 적절성과 제품의 친밀도는 제품 만족도에 정(正)의 영향을 미치치 않는다

> product <- read.csv("./data/product.csv", header=TRUE)
> head(product)
  제품_친밀도 제품_적절성 제품_만족도
1           3           4           3
2           3           3           2
3           4           4           4
4           2           2           2
5           2           2           2
6           3           3           3

> str(product)
'data.frame':	264 obs. of  3 variables:
 $ 제품_친밀도: int  3 3 4 2 2 3 4 2 3 4 ...
 $ 제품_적절성: int  4 3 4 2 2 3 4 2 2 2 ...
 $ 제품_만족도: int  3 2 4 2 2 3 4 2 3 3 ...

> y <- product$제품_만족도  # 종속변수
> x1 <- product$제품_적절성 # 독립변수1
> x2 <- product$제품_친밀도 # 독립변수2
> df <- data.frame(x1, x2, y)


# 다중 회귀 분석
> result.lm <- lm(formula=y~x1+x2, data=df)
> result.lm    # 절편(0.66731)과 기울기(x1:0.09593, x2:0.68522) 확인

Call:
lm(formula = y ~ x1 + x2, data = df)

Coefficients:
(Intercept)           x1           x2  
    0.66731      0.68522      0.09593  


# 다중 공선성문제 확인
> install.packages("car")
> library(car)

> vif(result.lm)  
# 분산팽창요인(VIF) - 결과값이 10 이상인 경우에는 다중 공선성문제를 의심해 볼수 있다. 
      x1       x2 
1.331929 1.331929 

# 다중 회귀 분석 결과 보기
> summary(result.lm)

Call:
lm(formula = y ~ x1 + x2, data = df)

Residuals:
     Min       1Q   Median       3Q      Max 
-2.01076 -0.22961 -0.01076  0.20809  1.20809 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.66731    0.13094   5.096 6.65e-07 ***
x1           0.68522    0.04369  15.684  < 2e-16 ***
x2           0.09593    0.03871   2.478   0.0138 *  
---
Signif. codes:  
0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.5278 on 261 degrees of freedom
Multiple R-squared:  0.5975,	Adjusted R-squared:  0.5945 
F-statistic: 193.8 on 2 and 261 DF,  p-value: < 2.2e-16

#Multiple R-squared:  0.5975,    Adjusted R-squared:  0.5945 
#F-statistic: 193.8 on 2 and 261 DF,  p-value: < 2.2e-16
#x1           0.68522    0.04369  15.684  < 2e-16 ***
#x2           0.09593    0.03871   2.478   0.0138 *  

# x1은 제품의 적절성이 제품 만족도에 미치는 영향 t검정통계량 15.684,
# x2는 제품의 친밀도가 제품 만족도에 미치는 영향 t검정통계량 2.478
# x1, x2의 유의 확률은 0.05보다 작기 때문에 제품 만족도에 양의 영향을 미친다. (연구가설 채택)
# 상관계수(결정계수) 0.5975는 다소 높은 상관관계를 나타낸다.
# 설명력은 59.45%
# 회귀모델의 적합성 f검정통계량은 193.8, p-value < 2.2e-16로 0.05보다 매우 낮으므로 이 회귀모델은 적합하다.
# 제품의 적절성(x1)이 제품의 만족도에 제품의 친밀성보다 더 영향력이 크다.
```



```R
############## 다중 공산성 문제 해결과 모델 평가 ##############
#iris의 Sepal.Length(꽃받침 길이)를 종속변수로 지정하고 Sepal.Width, Petal.Length, Petal.Width을 독립변수로 ..

> fit <- lm(formula= Sepal.Length ~ Sepal.Width+Petal.Length+Petal.Width, data=iris)
> fit

Call:
lm(formula = Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width, 
    data = iris)

Coefficients:
 (Intercept)   Sepal.Width  Petal.Length   Petal.Width  
      1.8560        0.6508        0.7091       -0.5565  


# 다중 공산성 문제 확인
> vif(fit)
 Sepal.Width Petal.Length  Petal.Width 
    1.270815    15.097572    14.234335 
# Petal, Length, Petal.Width 변수는 강한 상관관계로 인해서 다중 공산성 문제가 의심된다.


# 다중 공산성 문제가 의심되는 변수의 상관계수 확인
> cor(iris[, -5])
             Sepal.Length Sepal.Width Petal.Length Petal.Width
Sepal.Length    1.0000000  -0.1175698    0.8717538   0.8179411
Sepal.Width    -0.1175698   1.0000000   -0.4284401  -0.3661259
Petal.Length    0.8717538  -0.4284401    1.0000000   0.9628654
Petal.Width     0.8179411  -0.3661259    0.9628654   1.0000000


# 학습 데이터와 검정 데이터를 7:3으로 표본 추출
> x <- sample(1:nrow(iris), 0.7*nrow(iris)) # 70%에 해당하는 표본 추출
> train <- iris[x, ] # 학습 데이터
> test <- iris[-x, ] # 검정 데이터


# Petal.Width 변수를 제거한 후 학습데이터로부터 회귀모델 생성
> model <- lm(formula = Sepal.Length ~ Sepal.Width + Petal.Length, data=iris)
> model

Call:
lm(formula = Sepal.Length ~ Sepal.Width + Petal.Length, data = iris)

Coefficients:
 (Intercept)   Sepal.Width  Petal.Length  
      2.2491        0.5955        0.4719  

> summary(model)

Call:
lm(formula = Sepal.Length ~ Sepal.Width + Petal.Length, data = iris)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.96159 -0.23489  0.00077  0.21453  0.78557 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)   2.24914    0.24797    9.07 7.04e-16 ***
Sepal.Width   0.59552    0.06933    8.59 1.16e-14 ***
Petal.Length  0.47192    0.01712   27.57  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.3333 on 147 degrees of freedom
Multiple R-squared:  0.8402,	Adjusted R-squared:  0.838 
F-statistic: 386.4 on 2 and 147 DF,  p-value: < 2.2e-16

# 꽃받침의 너비가 꽃받침의 길이에 영향을 미친다.
# 꽃잎의 길이가 꽃받침의 길이에 영향을 미친다.
```



```R
############ 검정 데이터에 회귀모델 적용 예측값 생성 후 모델 평가 #############
> head(train, 1)
   Sepal.Length Sepal.Width Petal.Length Petal.Width    Species
55          6.5         2.8          4.6         1.5 versicolor

> Y=2.2491+0.5955*3.3 + 0.4719*5.7
> Y  # 회귀모델로부터 계산된 예측값
[1] 6.90408

# 오차 = 예측값 - 관측값
> 6.90408-6.7
[1] 0.20408

# stats::predict(model, data)
> pred <- predict(model, test)
> pred # 예측값 생성
       1        3        6        8       10       11       12       17       26 
4.994165 4.768315 5.373951 4.981804 4.803147 5.160462 5.028996 5.185183 4.790786 
      27       31       36       43       44       47       51       54       58 
5.028996 4.850339 4.721123 4.768315 5.088549 5.267206 6.372844 5.506527 5.235736 
      60       65       70       79       82       84       89       90       95 
5.697545 5.675074 5.578440 6.099802 5.424504 6.263849 5.970587 5.625632 5.839121 
      96      101      103      106      108      110      111      118      121 
6.017779 7.045892 6.820043 7.150387 6.949258 7.271741 6.561612 7.673998 6.844764 
     123      126      129      133      135      136      140      145      148 
7.078474 6.986340 6.559362 6.559362 6.440257 6.914427 6.643635 6.904316 6.489699

# 모델 평가는 상관계수를 이용해 모델의 정확도를 평가한다.
> cor(pred, test$Sepal.Length)
[1] 0.9513846
# 예측치와 실제 관측치는 상관계수가 0.9419519 이므로 매우 높은 상관관계를 보인다고 할 수 있으며, 모델의 정확도가 아주 높다고 볼 수 있다.
```



```R
################다중 회귀 분석 연습문제 #####################
# 01] product.csv 파일의 데이터를 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.
> product <- read.csv("./product2.csv", header=TRUE)
> str(product)
'data.frame':	264 obs. of  3 variables:
 $ 제품_친밀도: int  3 3 4 2 2 3 4 2 3 4 ...
 $ 제품_적절성: int  4 3 4 2 2 3 4 2 2 2 ...
 $ 제품_만족도: int  3 2 4 2 2 3 4 2 3 3 ...

# 단계1 : 학습데이터(train), 검정데이터(test)를 7 : 3 비율로 샘플링
> x <- sample(1:nrow(product), 0.7*nrow(product)) # 70%에 해당하는 표본 추출
> train <- product[x, ] # 학습 데이터
> test <- product[-x, ] # 검정 데이터

# 단계2 : 학습데이터 이용 회귀모델 생성
> model <- lm(formula = 제품_만족도 ~ 제품_친밀도 + 제품_적절성, data=train)
> model

Call:
lm(formula = 제품_만족도 ~ 제품_친밀도 + 제품_적절성, data = train)

Coefficients:
(Intercept)  제품_친밀도  제품_적절성  
    0.72401      0.08166      0.68397  

> summary(model)

Call:
lm(formula = 제품_만족도 ~ 제품_친밀도 + 제품_적절성, data = train)

Residuals:
     Min       1Q   Median       3Q      Max 
-2.02087 -0.25525 -0.02087  0.21351  1.21351 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.72401    0.16298   4.442 1.55e-05 ***
제품_친밀도  0.08166    0.04667   1.750   0.0819 .  
제품_적절성  0.68397    0.05283  12.947  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.5327 on 181 degrees of freedom
Multiple R-squared:  0.5757,	Adjusted R-squared:  0.571 
F-statistic: 122.8 on 2 and 181 DF,  p-value: < 2.2e-16


# 단계3 : 검정데이터 이용 모델 예측치 생성
> pred <- predict(model, test) # 예측치 생성


# 단계4 : 모델 평가 : cor() 함수 이용
> cor(pred, test$제품_만족도) # 모델 평가
[1] 0.8019507
# 예측치와 실제 관측치는 상관계수가 8019507 이므로 매우 높은 상관관계를 보인다고 할 수 있으며, 모델의 정확도가 아주 높다고 볼 수 있다.


02] ggplot2패키지에서 제공하는 diamonds 데이터 셋을 대상으로 carat, table, depth 변수
중 다이아몬드의 가격(price)에 영향을 미치는 관계를 다중회귀 분석을 이용하여 예측하
시오.
조건1) 다이아몬드 가격 결정에 가장 큰 영향을 미치는 변수는?
조건2) 다중회귀 분석 결과를 양(+)과 음(-) 관계로 해설
library(ggplot2)
data(diamonds)

# diamonds에서 비율척도 대상으로 식 작성
formula <- price ~ carat + table + depth
head(diamonds)
result <- lm(formula, data=diamonds)
summary(result) # 회귀분석 결과

#Coefficients:
#Estimate Std. Error t value Pr(>|t|)
#(Intercept) 13003.441 390.918 33.26 <2e-16 ***
#carat 7858.771 14.151 555.36 <2e-16 ***
#table -104.473 3.141 -33.26 <2e-16 ***
#depth -151.236 4.820 -31.38 <2e-16 ***
해설>carat은 price에 정(+)의 영향을 미치지만, table과 depth는 부(-)의 영향을 미친다.
```



##### 3. 로지스틱 회귀분석

- 종속변수와 독립변수 간의 관계를 예측모델로 생성 

- 독립변수(x)에 의해서 종속변수(y)의 범주로 분류하는 분류분석 방법

- 로지스틱 회귀 분석(Logistic Regression Analysis) 특징
  - 분석 목적 : 종속변수와 독립변수 간의 관계를 통해서 예측모델을 생성
  - 회귀분석과의 차이점 : 종속변수는 반드시 범주형 변수이어야 한다.  (이산형: Yes/No, 다항형: iris의 species 컬럼)
  - 정규성 : 정규분포 대신에 이항분포를 따른다.
  - 로짓 변환 : 종속변수의 출력범위를 0과 1로 조정하는 과정을 의미한다. (예: 혈액형 A인 경우 -> [1,  0, 0, 0]
  - 활용분야 : 의료, 통신, 날씨 등 다양한 분야에서 활용
- glm(y ~x, data, family)  이용하여  학습 데이터로부터 로지스틱 회귀모델  생성
- family의 ‘binormial’은 y변수가 이항형인 경우 지정하는 속성값
- x 변수의 유의성 검정을 제공하지만, F 검정 통계량과 모델의 설명력은 제공되지 않는다.
- 모델을 평가하기 위해서는 혼돈 매트릭스를 이용
- ROC Curve 패키지를 이용한 모델 평가 

```R
################# 로지스틱 회귀분석 #################
> weather <- read.csv("./data/weather.csv", stringsAsFactors = FALSE)
> dim(weather) # 관측치 366, 변수 15
[1] 366  15

> str(weather)
'data.frame':	366 obs. of  15 variables:
 $ Date         : chr  "2014-11-01" "2014-11-02" "2014-11-03" "2014-11-04" ...
 $ MinTemp      : num  8 14 13.7 13.3 7.6 6.2 6.1 8.3 8.8 8.4 ...
 $ MaxTemp      : num  24.3 26.9 23.4 15.5 16.1 16.9 18.2 17 19.5 22.8 ...
 $ Rainfall     : num  0 3.6 3.6 39.8 2.8 0 0.2 0 0 16.2 ...
 $ Sunshine     : num  6.3 9.7 3.3 9.1 10.6 8.2 8.4 4.6 4.1 7.7 ...
 $ WindGustDir  : chr  "NW" "ENE" "NW" "NW" ...
 $ WindGustSpeed: int  30 39 85 54 50 44 43 41 48 31 ...
 $ WindDir      : chr  "NW" "W" "NNE" "W" ...
 $ WindSpeed    : int  20 17 6 24 28 24 26 24 17 6 ...
 $ Humidity     : int  29 36 69 56 49 57 47 57 48 32 ...
 $ Pressure     : num  1015 1008 1007 1007 1018 ...
 $ Cloud        : int  7 3 7 7 7 5 6 7 7 1 ...
 $ Temp         : num  23.6 25.7 20.2 14.1 15.4 14.8 17.3 15.5 18.9 21.7 ...
 $ RainToday    : chr  "No" "Yes" "Yes" "Yes" ...
 $ RainTomorrow : chr  "Yes" "Yes" "Yes" "Yes" ...

> weather_df <- weather[, c(-1, -6, -8, -14)]


# y변수(RainTomorrow)의 로짓 변환 : (0, 1) 생성
> weather_df$RainTomorrow[weather_df$RainTomorrow=='Yes'] <- 1
> weather_df$RainTomorrow[weather_df$RainTomorrow=='No'] <- 0
> weather_df$RainTomorrow <- as.numeric(weather_df$RainTomorrow)
> head(weather_df)
  MinTemp MaxTemp Rainfall Sunshine WindGustSpeed
1     8.0    24.3      0.0      6.3            30
2    14.0    26.9      3.6      9.7            39
3    13.7    23.4      3.6      3.3            85
4    13.3    15.5     39.8      9.1            54
5     7.6    16.1      2.8     10.6            50
6     6.2    16.9      0.0      8.2            44
  WindSpeed Humidity Pressure Cloud Temp RainTomorrow
1        20       29   1015.0     7 23.6            1
2        17       36   1008.4     3 25.7            1
3         6       69   1007.2     7 20.2            1
4        24       56   1007.0     7 14.1            1
5        28       49   1018.5     7 15.4            0
6        24       57   1021.7     5 14.8            0


# 학습 데이터와 검정 데이터 생성(7:3)
> idx <- sample(1:nrow(weather_df), nrow(weather_df)*0.7)
> train <- weather_df[idx, ]
> test <- weather_df[-idx, ]

# 학습 데이터로부터 로지스틱 회귀모델 생성
> weather_model <- glm(formula=RainTomorrow ~ ., data=train, family='binomial')
> summary(weather_model)

Call:
glm(formula = RainTomorrow ~ ., family = "binomial", data = train)

Deviance Residuals: 
    Min       1Q   Median       3Q      Max  
-1.7985  -0.4066  -0.2100  -0.1012   2.6661  

Coefficients:
               Estimate Std. Error z value Pr(>|z|)   
(Intercept)   142.14170   54.30411   2.618  0.00886 **
MinTemp        -0.15884    0.08488  -1.871  0.06130 . 
MaxTemp         0.12205    0.27700   0.441  0.65948   
Rainfall       -0.12393    0.08529  -1.453  0.14622   
Sunshine       -0.30329    0.13704  -2.213  0.02689 * 
WindGustSpeed   0.08909    0.02839   3.138  0.00170 **
WindSpeed      -0.06769    0.04149  -1.631  0.10284   
Humidity        0.08063    0.03186   2.531  0.01138 * 
Pressure       -0.14943    0.05253  -2.845  0.00444 **
Cloud           0.04033    0.12813   0.315  0.75297   
Temp            0.11643    0.28385   0.410  0.68166   
---
Signif. codes:  
0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 220.53  on 251  degrees of freedom
Residual deviance: 126.52  on 241  degrees of freedom
  (4 observations deleted due to missingness)
AIC: 148.52

Number of Fisher Scoring iterations: 6
 
 
 
# 로지스틱 회귀모델 예측치 생성 
> pred <- predict(weather_model, newdata=test, type="response")
> pred # 예측치가 1에 가까울수록 비율 확률이 높다고 할 수 있다.
           1            2            4            5            6            8 
0.0446640503 0.0732972789 0.0013232314 0.0137058771 0.0419400042 0.0553630525 
           9           12           15           17           19           22 
0.1872863288 0.0295066137 0.0190619872 0.1840574329 0.0379876959 0.7151964833 
          23           24           28           29           30           31 
0.0823400296 0.0938687406 0.1675932652 0.8752290911 0.6225658521 0.4027907056 
          32           34           37           38           41           46 
0.1495715907 0.0700156437 0.7033561079 0.0947734191 0.2793926924 0.9217559450 
          50           51           52           53           56           57 
0.6717209528 0.2821342551 0.8454355873 0.0129787436 0.0139176880 0.4015116676 
          61           64           66           73           74           79 
0.0134185342 0.5194463666 0.1209133154 0.6908916828 0.3046156847 0.4040683683 
          82           84           89           91          101          106 
0.5323005920 0.0156234221 0.0190168879 0.6811565443 0.1432107689 0.0194066762 
         107          108          110          111          112          113 
0.0154325955 0.0125328320 0.0256498645 0.0365915090 0.3678232612 0.8895965448 
         115          118          124          131          137          139 
0.0472810472 0.0371753519 0.0262067978 0.0107366311 0.0098969831 0.0362668213 
         155          158          164          166          167          168 
0.0292772091 0.0151808675 0.1547896474 0.0036047961 0.0053383000 0.0038972431 
         171          175          178          182          183          185 
0.0115471761 0.0193305638 0.4246599717 0.0170748467 0.1055015288 0.0281495002 
         186          194          199          201          213          215 
0.0223252839 0.0092860100 0.8655075128 0.1522616046 0.0074221215 0.1278903721 
         216          220          225          235          237          240 
0.2012757755 0.0051230525 0.0152313314 0.0073786523 0.1457785596 0.0044339597 
         242          253          255          258          261          262 
0.0144050762 0.9483867709 0.0215263691 0.0447762234 0.4008225268 0.0144235577 
         264          265          267          273          280          281 
0.0222497208 0.0013417684 0.0072220021 0.0397851011 0.0242127124 0.3526320367 
         283          290          298          301          303          305 
0.1573016014 0.0070207258 0.0007586718           NA 0.0222140717 0.9802295441 
         312          316          323          324          330          335 
0.0316600700 0.0067536860 0.0261963273 0.0456686329 0.0018410476 0.0056591016 
         345          346          355          356          359          360 
0.0043162019 0.0018970968 0.0081304833 0.0286077768 0.0475045115 0.0349302578 
         364          366 
0.0665090083 0.1469651756 
 
# 예측치를 이항형으로 변환 : 0.5이상이면 1, 0.5미만이면 0
> result_pred <- ifelse(pred >= 0.5, 1, 0)
> result_pred
  1   2   4   5   6   8   9  12  15  17  19  22  23  24  28  29  30 
  0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   1   1 
 31  32  34  37  38  41  46  50  51  52  53  56  57  61  64  66  73 
  0   0   0   1   0   0   1   1   0   1   0   0   0   0   1   0   1 
 74  79  82  84  89  91 101 106 107 108 110 111 112 113 115 118 124 
  0   0   1   0   0   1   0   0   0   0   0   0   0   1   0   0   0 
131 137 139 155 158 164 166 167 168 171 175 178 182 183 185 186 194 
  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0 
199 201 213 215 216 220 225 235 237 240 242 253 255 258 261 262 264 
  1   0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0 
265 267 273 280 281 283 290 298 301 303 305 312 316 323 324 330 335 
  0   0   0   0   0   0   0   0  NA   0   1   0   0   0   0   0   0 
345 346 355 356 359 360 364 366 
  0   0   0   0   0   0   0   0 

> table(result_pred)
result_pred
 0  1 
94 15 

> table(result_pred, test$RainTomorrow)
result_pred  0  1
          0 80 14
          1  4 11

# 분류 정확도
> (80+11)/(84+14+4+11)
[1] 0.8053097
 
# ROC Curve 를 이용한 모델 평가
> install.packages("ROCR")
> library(ROCR)
> pr <- prediction(pred, test$RainTomorrow)
> prf <- performance(pr, measure="tpr", x.measure="fpr")
> plot(prf)
#왼쪽 상단의 계단모양의 빈 공백만큼이 분류 정확도에서 오분류(missing)를 나타낸다.
```

![6](190920%20R%20Statistics.assets/6.JPG)

