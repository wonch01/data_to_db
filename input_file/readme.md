### (개요) Input File 기능
- 원격 / 로컬 텍스트파일 read
  - 로컬 파일 : 경로 open 가능
  - 원격 : S3, Webdav 등의 프로토콜로 접근
- 텍스트파일 처리하여 JSON 형태로 저장
- JSON 파일 저장후, provide 방법
  - 정해진 directory에 JSON 파일 저장
  - JSON 파일명에 따른 sub directory 구분
  - provide 되는 JSON을 사용하는 코드에서는
    - JSON 파일 전체에 대한 경로 리스트를 이용하여,
    - 모든 파일에 대한 접근, 변경 등의 처리 진행  

### To Do which needs design and coding

#### (기능1) 원격 파일 접근 프로토콜
- S3 프로토콜
- Webdav 프로토콜 등


