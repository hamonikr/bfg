## bfg 스크립트 사용법

### 기본 사용법

```
bfg [옵션] [파라미터]
```
### 옵션
```
--clone REPO_URL: 지정한 Git 저장소를 클론합니다.
--find-big-files: 저장소에서 큰 파일을 찾습니다. (이 기능은 추가 구현이 필요합니다.)
--remove-big-files SIZE: 지정한 크기(SIZE MB)보다 큰 파일을 저장소에서 삭제합니다.
--push: 변경 내용을 원격 저장소에 푸시합니다.
```

### 예시
#### 저장소 클론:

```
./bfg --clone https://github.com/example/repo.git
```

#### 큰 파일 삭제 (예: 100MB 이상):

```
./bfg --remove-big-files 100
```

#### 변경 내용 원격 저장소에 푸시:

```
./bfg --push
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
