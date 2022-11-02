package template

type MyOTP interface {
	genRandomOTP(int) string
	saveOTPCache(string)
	getMessage(string) string
	sendNotification(string) error
}

type OTP struct {
	MyOTP MyOTP
}

func (o *OTP) GenAndSendOTP(optLength int) error {
	otp := o.MyOTP.genRandomOTP(optLength)
	o.MyOTP.saveOTPCache(otp)
	message := o.MyOTP.getMessage(otp)
	err := o.MyOTP.sendNotification(message)
	if err != nil {
		return err
	}
	return nil
}
