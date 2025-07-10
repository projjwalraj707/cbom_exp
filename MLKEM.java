import java.security.SecureRandom;

import org.bouncycastle.pqc.crypto.mlkem.MLKEMKeyGenerationParameters;
import org.bouncycastle.pqc.crypto.mlkem.MLKEMKeyParameters;
import org.bouncycastle.pqc.crypto.mlkem.MLKEMKeyPairGenerator;
import org.bouncycastle.pqc.crypto.mlkem.MLKEMParameters;

public class MLKEM {
	public static void main(String[] args) throws Exception {
		SecureRandom secureRandom = new SecureRandom();
		MLKEMKeyGenerationParameters mlkemKeyGenParam = new MLKEMKeyGenerationParameters(secureRandom, MLKEMParameters.ml_kem_768);
		MLKEMKeyPairGenerator mlKemKeyPairGen = new MLKEMKeyPairGenerator();
		mlKemKeyPairGen.init(mlkemKeyGenParam);
		var keyPair = mlKemKeyPairGen.generateKeyPair();
	}
}

