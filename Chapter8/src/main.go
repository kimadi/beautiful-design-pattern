package main

import (
	"beutiful-design-pattern/Chapter8/src/template"
	"fmt"
)

func main() {
	smsOTP := &template.Sms{}
	o := template.OTP{
		MyOTP: smsOTP,
	}
	o.GenAndSendOTP(4)

	emailOTP := &template.Email{}

	fmt.Println("-----------------------------")

	o = template.OTP{
		MyOTP: emailOTP,
	}
	o.GenAndSendOTP(4)
}
