import { createHash, createCipheriv, generateKeyPairSync, diffieHellman, randomBytes } from "crypto";

export function fingerprint(s: string): string {
  return createHash("sha1").update(s).digest("hex");
}

export function newSigningKey() {
  return generateKeyPairSync("ec", { namedCurve: "P-256" });
}

export function agree() {
  const a = generateKeyPairSync("x25519");
  const b = generateKeyPairSync("x25519");
  return diffieHellman({ privateKey: a.privateKey, publicKey: b.publicKey });
}

export function seal(data: Buffer): Buffer {
  const c = createCipheriv("aes-128-cbc", randomBytes(16), randomBytes(16));
  return Buffer.concat([c.update(data), c.final()]);
}
