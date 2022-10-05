package main

import (
	"beutiful-design-pattern/Chapter3/src/cipher"
	"beutiful-design-pattern/Chapter3/src/lzw"
	"fmt"
)

// 추상 데코레이터
type Component interface {
	Operator(string)
}

var sentData string
var recvData string

// 구상 구성요소
type SendComponent struct {
}

// 구상 구성요소
type ReadComponent struct {
}

// 구상 데코레이터
type ZipComponent struct {
	com Component
}

// 구상 데코레이터
type UnzipComponent struct {
	com Component
}

// 구상 데코레이터
type EncryptComponent struct {
	key string
	com Component
}

// 구상 데코레이터
type DecryptComponent struct {
	key string
	com Component
}

func (self *SendComponent) Operator(data string) {
	// 데이터 전송
	sentData = data
}

func (self *ZipComponent) Operator(data string) {
	zipData, err := lzw.Write([]byte(data))
	if err != nil {
		panic(err)
	}
	self.com.Operator(string(zipData))
}

func (self *EncryptComponent) Operator(data string) {
	encryptData, err := cipher.Encrypt([]byte(data), self.key)
	if err != nil {
		panic(err)
	}
	self.com.Operator(string(encryptData))
}

func (self *DecryptComponent) Operator(data string) {
	decryptData, err := cipher.Decrypt([]byte(data), self.key)
	if err != nil {
		panic(err)
	}
	self.com.Operator(string(decryptData))
}

func (self *UnzipComponent) Operator(data string) {
	unzipData, err := lzw.Read([]byte(data))
	if err != nil {
		panic(err)
	}
	self.com.Operator(string(unzipData))
}

func (self *ReadComponent) Operator(data string) {
	recvData = data
}

func main() {
	sender := &EncryptComponent{
		key: "abcde",
		com: &ZipComponent{
			com: &SendComponent{},
		},
	}

	sender.Operator("Hello World")

	fmt.Println(sentData)

	receiver := &UnzipComponent{
		com: &DecryptComponent{
			key: "abcde",
			com: &ReadComponent{},
		},
	}

	receiver.Operator(sentData)
	fmt.Println(recvData)
}
