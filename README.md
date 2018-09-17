# NNST - 한국어 네이버 뉴스 데이터셋

- Mnist같이 레이블링된 한국어 뉴스 데이터셋 (X,Y 형태) 을 제공하는 라이브러리 입니다.
- python3 버전 이상에서 동작합니다.
- y데이터의 매핑값은 다음과 같습니다.
    0: 정치, 1: 경제, 2: 사회, 3: 생활, 4: 세계, 5: IT/과학

## 설치
          pip install nnst

## 간단한 사용법
- csv파일 경로, 다운로드할 데이터 개수, 트레이닝셋 사이즈, 기사 등록 날짜를 지정하여 다음을 실행합니다.

           $project_root > python example/example.py --csv_path {저장할 csv파일 경로}  --num {다운로드할 각 카테고리당 데이터 개수} --num_train {트레이닝 데이터 개수} --date {가장 최신 기사 날짜}
- 이 파일을 실행하면, 파일을 다운로드 한 뒤, train_set,test_set,random_batched_set을 각각 출력 합니다.


           $project_root > python example/example.py --csv_path csv/save.csv  --num 200 --num_train 100 --date 20180908
           ...
           [Progress] 97.16666666666667 % download complete
           [Progress] 97.66666666666667 % download complete
           [Progress] 98.13333333333333 % download complete
           [Progress] 98.61666666666666 % download complete
           [Status] ----- category Tech download complete -----
           [Success] All download was complete

           ------train set------
           array([['수십억 들인 한강예술공원 작품… 시민들  흉물같다 ', '2'],
               ['5G 기술기준 확정···상용화 탄력', '5'],
               ['미 중간선거 이전…트럼프  워싱턴으로 김정은 초청할까', '0'],
               ...,
               ['오스트리아 빈  세계에서 가장 살기 좋은 도시 1위', '4'],
               ['스마트폰 ‘괴물급’ 배터리 전쟁', '5'],
               [' 화이트리스트  김기춘 징역 4년·조윤선 징역 6년 구형', '0']], dtype='<U74')
           ---------------------

           ------test  set------
           array([[' 9·13대책 Q A  서울 시가 19억원 2주택 종부세…187만→415만원', '0'],
                ['허벅지에 찰흙 붙이고 머리엔 스펀지…병역기피  꼼수 ', '0'],
                [' 종합 이 총리  금리 문제  어느 쪽이라는 말은 안했다…금통위 독립성 보장 ', '0'],
                ...,
                ['셀카봉 없이  찰칵 ···가장 먼저 눈길 간 갤노트9  S펜 ', '5'],
                [' 포트나이트 여기 없어요  경고문 띄운 구글', '5'],
                ['갤럭시노트9 써 보니…핵심은 역시  S펜    ABCD 는 덤', '5']], dtype='<U74')
           ---------------------

           ------batch set------
           array([[['서울만 벗어나면 미분양 속출…집값 양극화 극심', '1'],
                   [' 종합2보  거가대교서 5시간 동안 음주난동 벌인 트레일러 기사 검거', '2'],
                   [' 이철재의 밀담  총 처음 만져도 명사수 된다   육군  워리어 플랫폼 의 마술', '0'],
                   ...,
                   ['임종석  한국정치의 꽃할배이길 …중진론 앞세워 거듭 방북 요청', '0'],
                   ['김현미  임대사업자 세제혜택 축소…세금감소분 갭투자 악용 ', '1'],
                   ['내 집 짓고 싶은데 아무것도 모르는 초보라면…', '3']],

                  [['아파트 코앞 애견 운동장… 개들은 천국  주민엔 소음지옥', '2'],
                   [' 이산가족상봉  눈물도 마른 101세 백성규옹  北손녀에 담담한 미소', '0'],
                   ['트럼프  폼페이오 방북 취소…중국이 안 도와줄 것 같아 ', '4'],
                   ...,
                   ['통신 3사  5G장비 업체 이달 선정… 뜨거운 감자  화웨이', '5'],
                   [' 유튜브 쇼크①   갓튜브  대항할 자가 없다', '5'],
                   ['오바마  트럼프 실명비판… 보수주의도  정상도 아니다 ', '4']],
                   ...

## 뉴스 데이터 파일 다운로드
           > import nnst.downloader as downloader
           > downloader.download(데이터 개수, csv파일 경로, 최신 뉴스 날짜)

* 실행 결과:

           ...
           [Progress] 97.16666666666667 % download complete
           [Progress] 97.66666666666667 % download complete
           [Progress] 98.13333333333333 % download complete
           [Progress] 98.61666666666666 % download complete
           [Status] ----- category Tech download complete -----
           [Success] All download was complete

## 데이터 다루기(nnst)
           > import nnst.nnst as nnst
           > dataset = nnst.load_data(csv파일 경로)     #((X1, Y1), (X2,Y2),...)
           > dataset = nnst.div_dataset(dataset, 트레이닝셋 사이즈)     #(train dataset, test dataset)
           > dataset = nnst.random_batch(dataset[0], 1batch의 사이즈)       #(batch data1, batch data2, ... )

## License

Project is published under the MIT licence. Feel free to clone and modify repo as you want, but don'y forget to add reference to authors :)