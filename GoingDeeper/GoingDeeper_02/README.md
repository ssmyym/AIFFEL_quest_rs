# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 윤철희
- 리뷰어 : 최세영


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
  ![image](https://github.com/user-attachments/assets/8745be97-3c46-42ed-aa00-2d5bd902a5a0)
         -  결과가 잘 나왔고 "강건성과 성능은 trade-off 관계" 라는 결과를 도출하였습니다.

- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
![image](https://github.com/user-attachments/assets/a17355cf-d073-45fb-b6ff-4464bfc8e48f)
         -  예시 코드 말고도 다른 코드들을 봤을 때에도 중간 중간 설명을 잘 적으셨습니다. 

- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
![image](https://github.com/user-attachments/assets/4a231114-7632-46b0-9df2-46ba2cadf563)
         -  기본 augumentation 말고 gaussian noise를 사용하셔서 새로운 시도를 하셨습니다.

- [O]  **4. 회고를 잘 작성했나요?**
         -  ![image](https://github.com/user-attachments/assets/fa9f55c5-58de-43dd-9255-582a843e5be4)
         -  추가 실험을 계획하고 이번 실험 결과를 바탕으로 아쉬운 점도 잘 작성되었습니다.

- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
![image](https://github.com/user-attachments/assets/9dd7b27d-9c30-4568-a7de-cef2dc319751)
![image](https://github.com/user-attachments/assets/bc77a8c1-27a1-462a-a542-9babb95b9349)
        -  이렇게 모듈 임포트 부분도 중복되지 않게 잘 설정하셨고, 파트를 나눠서 잘 함수화 하였습니다.


# 회고(참고 링크 및 코드 개선)
```
철희님은 아주 깔끔하게 정리를 잘 하시는 것 같습니다. 또, 저는 csv_logger callback을 사용해본 적 없는데 이를 통해 더 좋은 시각화나 정보저장이 가능하다는 것을 알게되었습니다.
```
