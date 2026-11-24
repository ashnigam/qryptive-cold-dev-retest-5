package main

import (
	"crypto/ecdh"
	"crypto/md5"
	"crypto/rand"
	"crypto/rsa"
	"crypto/tls"
	"fmt"
)

func main() {
	rk, _ := rsa.GenerateKey(rand.Reader, 2048)
	xk, _ := ecdh.X25519().GenerateKey(rand.Reader)
	fmt.Println(rk.N.BitLen(), xk.PublicKey(), md5.Sum([]byte("x")))
	cfg := &tls.Config{MinVersion: tls.VersionTLS11}
	_ = cfg
}
