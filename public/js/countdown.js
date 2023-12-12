(function($) {
	$.fn.koreanTime = function() {
	  thisEl = $(this);
  
	  function updateKoreanTime() {
		var now = new Date();
		now.setUTCHours(now.getUTCHours()); // 한국 시간으로 변환
  
		var hours = now.getHours();
		var minutes = now.getMinutes();
		var seconds = now.getSeconds();
  
		// 한 자리 숫자의 경우 앞에 0을 붙여 두 자리로 표시
		hours = (hours < 10) ? '0' + hours : hours;
		minutes = (minutes < 10) ? '0' + minutes : minutes;
		seconds = (seconds < 10) ? '0' + seconds : seconds;
  
		// 한국 시간을 실시간으로 표시
		thisEl.find(".hours").text(hours);
		thisEl.find(".minutes").text(minutes);
		thisEl.find(".seconds").text(seconds);
	  }
  
	  // 초기 한 번 업데이트하고, 1초마다 업데이트
	  setInterval(updateKoreanTime, 1000);
	}
  })(jQuery);
  