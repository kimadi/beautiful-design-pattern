package lzw

import (
	"bytes"
	"compress/lzw"
	"fmt"
	"io/ioutil"
)

// lzw를 이용하여 데이터 압축
func Write(data []byte) ([]byte, error) {
	buf := new(bytes.Buffer)
	writer := lzw.NewWriter(buf, lzw.LSB, 8)
	n, err := writer.Write(data)
	if n != len(data) {
		return nil, fmt.Errorf("Not enough write:%d dataSize:%d", n, len(data))
	}
	if err != nil {
		return nil, err
	}
	writer.Close()
	return buf.Bytes(), nil
}

// lzw를 이용하여 압축 해제
func Read(data []byte) ([]byte, error) {
	r := bytes.NewReader(data)
	reader := lzw.NewReader(r, lzw.LSB, 8)
	origData, err := ioutil.ReadAll(reader)
	if err != nil {
		return nil, err
	}
	return origData, nil
}
