from django import forms


class OrderForm(forms.Form):
    user = forms.IntegerField(label="주문자")
    sender_name = forms.CharField(label="주문자 명", max_length=100)
    sender_email = forms.EmailField(label='주문자 이메일')
    sender_phone_number = forms.CharField(label='주문자 전화번호', max_length=50)

    receiver_name = forms.CharField(label='받는사람')
    receiver_phone_number = forms.CharField(label='받는사람 전화번호', max_length=50)
    receiver_address = forms.CharField(label='받는사람 주소', max_length=250)
    delivery_message = forms.CharField(label="배송 메시지")

    pay_type = forms.ChoiceField(label='결제방법', choices=[('0', '무통장입금'),
                                                        ('1', '휴대폰소액결제'),
                                                        ('2', '실시간계좌이체'),
                                                        ('3', '신용카드결제'),
                                                        ('4', '카카오페이')])
