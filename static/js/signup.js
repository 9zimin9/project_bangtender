document.addEventListener('DOMContentLoaded', function() {
    // 보유한 술 검색
    document.getElementById('search-alcohol').addEventListener('input', function() {
        const query = this.value;
        searchAlcohol(query, 'alcohol-results', 'selected-alcohols');
    });

    // 좋아하는 술 검색
    document.getElementById('search-favorite').addEventListener('input', function() {
        const query = this.value;
        searchAlcohol(query, 'favorite-results', 'selected-favorites');
    });

    // 싫어하는 술 검색
    document.getElementById('search-disliked').addEventListener('input', function() {
        const query = this.value;
        searchAlcohol(query, 'disliked-results', 'selected-disliked');
    });

    function searchAlcohol(query, resultId, selectedId) {
        // 여기에 검색 API 연결 필요 (가상 데이터를 사용)
        const results = ['술1', '술2', '술3'].filter(item => item.includes(query));

        const resultDiv = document.getElementById(resultId);
        resultDiv.innerHTML = ''; // 이전 결과 초기화

        results.forEach(item => {
            const button = document.createElement('button');
            button.textContent = item;
            button.classList.add('btn-liquor');
            button.addEventListener('click', function() {
                selectAlcohol(item, selectedId);
            });
            resultDiv.appendChild(button);
        });
    }

    function selectAlcohol(item, selectedId) {
        const selectedDiv = document.getElementById(selectedId);
        const span = document.createElement('span');
        span.textContent = item;
        selectedDiv.appendChild(span);
    }
});
