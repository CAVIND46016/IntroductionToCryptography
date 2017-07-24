//Name: Cavin Dsouza
//Email: dsouzac@indiana.edu

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;

public class ExplicitCTRClient
{
	public static void main(String [] args) throws IOException
	{
		String hostname = "burrow.soic.indiana.edu";
		int port = 33336;
		
		File file = new File("ctr-ciphertext");
		FileInputStream fin = new FileInputStream(file);

		int length = (int)file.length();
		byte [] ciphertext = new byte[length];
		fin.read(ciphertext);
		fin.close();

		Socket oracle = new Socket(hostname, port);
		DataOutputStream out = new DataOutputStream(oracle.getOutputStream());
		DataInputStream in = new DataInputStream(oracle.getInputStream());

		byte pad = 0;
		byte copy_ciphertext[] = new byte[length];

		// determine padding byte
		while (true)
		{
			System.arraycopy(ciphertext, 0, copy_ciphertext, 0, length);
			int last_idx = length - pad - 1;
			copy_ciphertext[last_idx] =  (byte) ((copy_ciphertext[last_idx] + 1) % 256);
			//System.out.println(copy_ciphertext);
			out.writeInt(length);
			out.write(copy_ciphertext);
			out.flush();

			byte response = in.readByte();
			if(response == 0)
			{
				pad = (byte) ((pad + 1) % 256);
				//System.out.println(pad);
			} 
			else 
			{
				break;
			}
		}

		System.out.println("padding is " + (pad) + " bytes of " + (pad-1));
		int plength = length - pad;
		System.out.println("plaintext length is " + (length - 17 - pad));
		
		char [] plaintext = new char[plength];
		for (int i = 0; i < plength; i++)
		{
			plaintext[i] = '_';
		}
		
		byte tmp_arr[] = new byte[length];
		for(int ctr = length - 1; ctr >= length - pad; ctr--)
		{
			tmp_arr[ctr] = (byte)(ciphertext[ctr] ^ (pad - 1));
		}
	
		// determine the non-padding bytes

		for(int i = 1; i < plength; i++)
		{
			System.arraycopy(ciphertext, 0, copy_ciphertext, 0, length);
			for(int j = length - 1; j > (length - pad - i); j--)
			{
				copy_ciphertext[j] = (byte) (tmp_arr[j] ^ (pad + i - 1));
			}
			while(true)
			{
				int last_idx = length - pad - i;
				copy_ciphertext[last_idx] = (byte) ((copy_ciphertext[last_idx] + 1) % 256);
				out.writeInt(length);
				out.write(copy_ciphertext);
				out.flush();

				byte response = in.readByte();
				if(response == 1)
				{
					tmp_arr[last_idx] = (byte) (copy_ciphertext[last_idx] ^ (pad+i-1));
					plaintext[plength - i] = (char)(ciphertext[last_idx] ^ tmp_arr[last_idx]);
					for(int k = 0; k < plength; k++)
					{
						System.out.print(plaintext[k]);
					}
					System.out.print("\n");
					break;
				}
			}
		}
		oracle.close();
	}
}