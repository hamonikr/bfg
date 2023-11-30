## bfg 

이 프로젝트는 BFG Repo-Cleaner 를 하모니카 OS 에서 쉽게 사용하기 위한 패키지 입니다.

BFG Repo-Cleaner는 Git 저장소의 히스토리에서 불필요한 또는 민감한 데이터를 제거하는 도구입니다. 

이 도구는 git-filter-branch의 대안으로 사용되며, 큰 파일, 비밀번호, 인증 정보 등을 빠르고 쉽게 제거할 수 있습니다. 

주요 특징은 다음과 같습니다:
- 속도: BFG는 git-filter-branch보다 10~720배 빠릅니다.
- 간단함: 특정 작업에 중점을 둬서 사용하기 쉽습니다.

## 언제 이 프로그램을 사용해야 하나요?

* 데이터 정리: Git 저장소의 히스토리에 민감한 정보(비밀번호, API 키 등)나 불필요한 큰 파일이 포함되어 있을 경우, 이를 제거해야 할 필요가 있습니다.

* 저장소 크기 최적화: 큰 파일이나 불필요한 데이터를 제거함으로써 저장소의 크기를 줄일 수 있습니다. 이는 클론 속도를 높이고, 저장소를 관리하기 쉽게 만듭니다.

* 보안: 민감한 정보가 공개 저장소에 노출되면 보안 위험이 발생할 수 있습니다. BFG를 사용하면 이러한 정보를 효과적으로 제거할 수 있습니다.

* 성능: git-filter-branch와 비교하여 BFG는 훨씬 빠른 성능을 제공합니다. 따라서 대규모 저장소에서도 빠르게 작업을 수행할 수 있습니다.

* 사용 편의성: BFG는 사용하기 쉬운 명령어와 옵션을 제공하여, 복잡한 명령어 없이도 원하는 작업을 쉽게 수행할 수 있습니다.

* 코드 품질 유지: 불필요한 파일이나 데이터를 제거함으로써 코드 품질을 유지할 수 있습니다.

## 기본 사용법

```
bfg [옵션] [파라미터]
```
### 옵션
```
--clone REPO_URL: 지정한 Git 저장소를 클론합니다.

--find-big-files SIZE REPO_PATH: 지정한 크기보다 큰 파일을 저장소에서 찾습니다.

--remove-big-files SIZE REPO_PATH: 지정한 크기보다 큰 파일을 저장소에서 삭제합니다.

--push REPO_PATH: 변경 내용을 원격 저장소에 푸시합니다.

--delete-files FILE_PATTERN  REPO_PATH : 저장소에서 FILE_PATTERN 에 해당하는 파일을 삭제합니다. 파일명 또는 파일명 패턴을 사용할 수 있습니다.

--replace-text WORD_LIST_FILE  REPO_PATH : 저장소에서 WORD_LIST_FILE 안의 단어를 찾아서 ***REMOVED*** 로 변경합니다.

```

### 예시
#### 저장소 클론:

```
./bfg --clone https://github.com/example/repo.git
```


#### 큰 파일 찾기 (예: 10MB 이상):

```
./bfg --find-big-filess 10M <REPO_PATH>
```

#### 큰 파일 삭제 (예: 100MB 이상):

```
./bfg --remove-big-files 100M <REPO_PATH>
```

#### 파일명이 id_dsa 또는 id_rsa 인 파일을 삭제:

```
./bfg --delete-files id_{dsa,rsa} <REPO_PATH>
```

#### 지정한 password.txt 파일에 있는 단어를 찾아서 ***REMOVED*** 로 변경:

```
./bfg --replace-text password.txt <REPO_PATH>
```

#### 변경 내용 원격 저장소에 푸시:

```
./bfg --push <REPO_PATH>
```

#### 모든 작업을 한 번에 수행:

```
./bfg --clone https://github.com/example/repo.git --remove-big-files 100 --push
```

#### 자동 완성
새 터미널 세션에서 bfg 명령어를 입력하고 탭키를 누르면 옵션을 자동 완성할 수 있습니다.

## debian 패키지 제작
```
dpkg-buildpackage
```

## More

보다 다양한 옵션을 확인하시려면 아래 프로젝트를 참고하세요.

BFG Repo-Cleaner : https://rtyley.github.io/bfg-repo-cleaner/
