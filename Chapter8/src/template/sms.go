package template

import "fmt"

type Sms struct {
	OTP
}

func (s *Sms) genRandomOTP(len int) string {
	randomOTP := "qkrqudcks7"
	fmt.Printf("SMS: 랜덤 OTP 생성: %s\n", randomOTP)
	return randomOTP
}

func (s *Sms) saveOTPCache(otp string) {
	fmt.Printf("SMS: OTP %s 저장!\n", otp)
}

func (s *Sms) getMessage(otp string) string {
	return "SMS: 내 OTP는" + otp
}

func (s *Sms) sendNotification(message string) error {
	fmt.Printf("SMS: %s\n", message)
	return nil
}
