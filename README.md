
  # 🚩 project Uhwa_Backend 
  ## 👩‍💻 A2 일석이조

   <a href="https://imgbb.com/"><img src="https://i.ibb.co/Lttj91M/123456.jpg" alt="123456" border="0"></a>
  <p>
      <img src="https://img.shields.io/badge/Django-4.1.1-green"/>
  </p>

  ###  소개
  - 이미지와 모델링을 통해서 사용자가 원하는 옷을 제작하고 사고 팔수 있는 사이트 
  - 노션 : https://www.notion.so/U-HWA-eb98ee6099534970839f78b5bac9eac8
  
  ###  사용한 데이터셋 모델
  - 스파르타 강의 에 포함되어있는 모델
  https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/dl/week02/instance_norm.zip
  
  ###  주요 기능 
  - ##### 로그인,회원가입 (정규식 on)
  - ##### 원하는 이미지 모델링 + 옷 합성된 사진 업로드 기능
  - ##### 게시글에 댓글작성,수정,삭제 기능
  - ##### 게시글에서 주문 기능
  - ##### 마이프로필에서 회원정보수정 기능,내가 북마크한 게시글과,내가 판매(게시한)한 글 모아보기 기능
  - ##### 주문 상태 변경 가능
  
  
  ***


  ###  개발 일정
  
  **진행기간** 2022년 11월 22일 ~ 2022년 11월 28일

  **11월 22~3일** S.A 내용 작성,와이어 데이터 베이스 불러오기 

  **11월 23~24일** 회원가입,로그인,회원정보 수정 기능 구현 ,딥러닝 구현

  **11월 25~26일** 게시글 상세 페이지,리뷰작성,수정,삭제,게시글 북마크 기능

  **11월 27~28일** 북마크 기능,배포,
  
  **11월 28일** 문서작업 및 QA 와 발표


  ### 프로젝트 참여한 명단 및 역할

  안범기: 딥러닝
  
  박효진 : 회원가입,로그인,회원정보 수정
  
  장준표 : 프론트(https://github.com/onestone2team/Uhwa_Frontend)
  
  김명현 : 게시글 생성,수정,게시글,북마 모아보기,
  
  유승주 : 댓글생성,수정,삭제

  ***
  
    
    
  ##  구상도
  <a href="https://ibb.co/Qp7RLH5"><img src="https://i.ibb.co/5GXymj7/1.png" alt="1" border="0"></a>
   ##  회원가입 페이지,로그인페이지
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/FhGcrgs/2.png" alt="2" border="0"></a>
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/SmR26YL/3.png" alt="3" border="0"></a>
   ##  메인 페이지
  <a href="https://ibb.co/9Zvq21N"><img src="https://i.ibb.co/0sXfZ6c/4.png" alt="4" border="0"></a>
   ## 제작 페이지
  <a href="https://ibb.co/bmVrgsV"><img src="https://i.ibb.co/ZXrh6Br/5.png" alt="5" border="0"></a>
   ##  상세 페이지
  <a href="https://ibb.co/TbH8X9y"><img src="https://i.ibb.co/3M0NXgK/6.png" alt="6" border="0"></a>
   ##  회원 정보
  <a href="https://ibb.co/PNFkCWQ"><img src="https://i.ibb.co/vHV9zdY/7.png" alt="7" border="0"></a>
   ##  북마크한 게시글 모아보기
  <a href="https://ibb.co/QvZtgyR"><img src="https://i.ibb.co/YB6wCHM/8.png" alt="8" border="0"></a>
   ##  주문들어온 품목 
  <a href="https://ibb.co/zHgfhH5"><img src="https://i.ibb.co/BKJsVKP/9.png" alt="9" border="0"></a>
    
    
  </div>
  </details>

  ###  erd

 <a href="https://ibb.co/yfzFRzg"><img src="https://i.ibb.co/TvQMTQP/erd1.png" alt="erd1" border="0"></a>
  


  <br/>
  
  <트러블슈팅>
 <details>
    <summary>안범기</summary>
    <img src=https://user-images.githubusercontent.com/105624323/204091176-9e5f753e-bfb1-4f71-931e-3d78b4d61c80.png>
    <br>머신러닝을 돌릴 때와 글 작성할때 필요한 인자 값이 달라서 각 각의 serializer을 생성
    <br><img src=https://user-images.githubusercontent.com/105624323/204091287-f0575fa1-a443-409e-a7ae-2d47eb220d2f.png>    
    <br><img src=https://user-images.githubusercontent.com/105624323/204091446-2b5b7d92-69ab-4566-9834-d47ad744f905.png>    
    <br>절대경로로 만들어서 깃에 올릴떄마다 변경해주어야하는 불편했던것을   
    <br><img src=https://user-images.githubusercontent.com/105624323/204091515-7042f383-6250-4c2c-a080-be8956ba76ad.png>   
    <br>슬라이싱을이용해서 팀원마다 경로 설정안하게 변경
    <br>
    <br>배포시 생기는 오류:libGL.so.1: cannot open shared object file: No such file or directory
    <br>오류 원인: opencv module이 설치되어있지 않아서 생기는 오류
    <br>DockerFile에
    <br>RUN apt-get update
    <br>RUN apt-get -y install libgl1-mesa-glx
    <br>넣으면 해결
    <br><img src=https://user-images.githubusercontent.com/105624323/204092285-06ee0c7a-d1f6-48c0-b2da-a2988eb4e3e8.png>
    
 </details>
 <details>
    <summary>박효진</summary>
    여기에 작성해주세요
 </details>
 <details>
    <summary>장준표</summary>
    여기에 작성해주세요
 </details>
 <details>
    <summary>김명현</summary>
    여기에 작성해주세요
 </details>
 <details>
    <summary>유승주</summary>
    여기에 작성해주세요
 </details>
  
  

