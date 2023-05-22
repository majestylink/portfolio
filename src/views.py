from django.shortcuts import render
from django.views import View


class Index(View,):

    def get_context(self):
        pass
        # active_coupons = Coupon.objects.filter(active=True).count()
        # used_coupons = Coupon.objects.filter(active=False).count()
        # total_generated_coupons = Coupon.objects.filter(user=self.request.user).count()
        # coupon_history = Coupon.objects.order_by('-created', '-updated')
        # # print(coupon_history)

        return

    def get(self, request, **kwargs):
        return render(request, 'index.html', self.get_context())

    # def post(self, request, **kwargs):
        # form_data = AffiliateCouponCreateForm(request.POST)
        # if form_data.is_valid():
        #     form_data = form_data.save(self.request.user.username)
        #
        #     if request.POST['provider'] == 'Credit/Debit':
        #         messages.success(request, 'Congratulations, OnClick you would be Redirected to make Payment')
        #         return redirect('src:gtgatway')
        #
        #     elif request.POST['provider'] == 'Paystack':
        #         from src.utills.provider import Paystack
        #         import json
        #         amount = IpCurrency(self.get_ip_address(request), round(form_data.amount.amount))
        #         data = {
        #             'email': self.request.user.email,
        #             'amount': str(amount.get_value() * 100),
        #         }
        #         data = json.dumps(data)
        #         pay = Paystack()
        #         status, url = pay.transact(data=data, pay=pay)
        #         if status:
        #             form_data.random = status['data']
        #             form_data.save()
        #         link = url
        #         return JsonResponse({'link': link}, status=200)
        #
        #     elif request.POST['provider'] == 'Flutterwave':
        #         from src.utills.provider import Flutterwave
        #         import json
        #         amount = IpCurrency(self.get_ip_address(request), round(form_data.amount.amount))
        #         data = {
        #             "redirect_url": reverse('src:rave'),
        #             # "payment_options": "card",
        #             'amount': str(round(form_data.amount.amount)),
        #             'currency': 'USD',
        #             'payment_plan': 16646,
        #             'tx_ref': str(form_data.unique_id),
        #             "customer": {
        #                 "email": self.request.user.email,
        #                 "name": self.request.user.username,
        #             },
        #             "customizations": {
        #                 "title": "TraffikBoss.com",
        #                 "description": "",
        #                 "logo": ""
        #             }
        #         }
        #         data = json.dumps(data)
        #         pay = Flutterwave()
        #         status, url = pay.transact(data=data, pay=pay)
        #         if status:
        #             form_data.random = status['data']
        #             form_data.save()
        #         link = url
        #         return JsonResponse({'link': link}, status=200)
        #
        # else:
        #     messages.error(request, form_data.errors)
        #     return JsonResponse({'errors': str(form_data.errors)}, status=400)
        #
        # return redirect('src:gen-coupon')


