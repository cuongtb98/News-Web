from underthesea import classify
from rake_nltk import Rake
text = '''
Khi châu Âu dự định mở cửa biên giới vào mùa hè này, Capri đã "đi trước một bước" với lời giới thiệu hấp dẫn: hòn đảo không có Covid-19. Capri, nằm trên vịnh Naples thuộc vùng Campania, thường được biết đến là nơi yêu thích của những du khách thượng lưu. Nhưng năm nay, thay vì quảng cáo những khách sạn sang trọng với tầm nhìn tuyệt đẹp ra biển, giới chức đưa ra một thông điệp đơn giản nhưng thành công hơn nhiều. Đó là: mọi người dân trên đảo đều đã được tiêm vaccine và nơi này "không có Covid-19", theo lời Vincenzo De Luca, người đứng đầu vùng Campania. Chúng tôi đang chuẩn bị chào đón hàng triệu khách du lịch, và ngăn họ đến Tây Ban Nha hay Hy Lạp nghỉ dưỡng. Bây giờ, điều cần thiết nhất là không lãng phí thời gian. Ngành khách sạn phải đưa ra quyết định trong tháng 5, nếu không chúng ta sẽ mất cả một mùa du lịch", De Luca nói trong một bài phát biểu vào 8/5
'''
# a = classify('Liệu trong thời gian 10 giây ngắn ngủi đó bạn có tìm ra được đáp án mà không phải ai cũng biết.')
# print(a)
import requests
q = 
r = Rake(min_length=2, max_length=5)
r.extract_keywords_from_text(q)
a = r.get_ranked_phrases()
b = r.get_ranked_phrases_with_scores()
print(b)