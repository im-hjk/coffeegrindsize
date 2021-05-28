To open the application simply launch the .app file located at /App/dist/coffeegrindsize.app

#간편사용설명서
본 설명서는 https://github.com/Coffee-Grind-Distribution/coffee-grind-distribution 에서 Instructions 부분을 참고해서 제작했습니다.

1. 흰색 A4용지를 준비한다. (없으면 아무 흰 종이와 자 혹은 동전를 준비한다)
2. 커피 그라인더에 최소한의 원두 (1 ~ 2알)을 투입해 커피가루를 만든다.
3. 미리 준비해둔 종이에 커피가루를 털어내고, 젓가락등을 사용해서 최대한 가루가 겹치지 않고 고르게 분포되도록 해준다.(예시 그림 : https://i.imgur.com/A1C2RPA.jpg
4. A4용지라면 용지 전체가 잘 나오도록, 아니면 종이 위에 자/동전을 같이 올리고 그림자가 지지 않게 바로 위에서 수직으로 사진을 찍는다.
5. coffeegrindsize app 을 실행하고 다음 순서대로 진행한다.
	- 5-1.  [Open image] 버튼을 누르고 방금 찍은 사진을 선택한다.
	- 5-2.  [Select Reference Object]을 누르고 A4용지를 사용했다면 용지의 한쪽 변을, 자나 동전을 사용한다면 자에서 1cm 눈금만큼 아니면 동전의 지름을 선으로 그려준다.
	- 5-3.  좌측에 [Reference Physical Size]을 입력하는 부분에 
		        A4용지라면 해당하면 변의 길이를 (210 x 297 mm)
		        자를 사용하면 10mm
		        동전을 사용하면 해당 동전의 지름을 (100원은 24mm, 500원은 26.5mm)
	        입력해준다
	- 5-4.  [Threshold Image]를 누르고 잠시 기다린다. (만약 시간이 너무 걸리거나 먹통이 되었다면 프로그램 종료 후 다시 시작하고 <5-2> 진행하기 이전 [Reduce Image Quality]을 1~2번 누른 뒤 진행한다)
	- 5-5.  [Launch Particle Detection]를 누르고 기다린다.
	- 5-6.  이후 화면에 인식된 커피가루가 빨강색 태두리로 표시되는데, 만약 뭉처있는 가루들이 있다면 [Erase Clusters]버튼을 누르고 해당 부분들을 이미지에서 클릭해 제거해준다.
	- 5-7.  [Create Histogram]을 누르고 기다린다.
	- 5-8.  [Save View]버튼으로 생성된 히스토그램을 저장하고, [Save Data]버튼으로 측정된 데이터를 .csv로 저장한다.
