package template

import "fmt"

type Email struct {
	OTP
}

func (e *Email) genRandomOTP(len int) string {
	randomOTP := "qkrqudcks7"
	fmt.Printf("Email: 랜덤 OTP 생성: %s\n", randomOTP)
	return randomOTP
}

func (e *Email) saveOTPCache(otp string) {
	fmt.Printf("Email: OTP %s 저장!\n", otp)
}

func (e *Email) getMessage(otp string) string {
	return "Email: 내 OTP는" + otp
}

func (e *Email) sendNotification(message string) error {
	fmt.Printf("Email: %s\n", message)
	return nil
}
