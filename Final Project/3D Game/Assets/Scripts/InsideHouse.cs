using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class InsideHouse : MonoBehaviour {

	void OnCollisionEnter (Collision other) {
		if (other.gameObject.tag == "Player") {
			if (SceneManager.GetActiveScene().name == "Inside" || SceneManager.GetActiveScene().name == "Inside2")
				SceneManager.LoadScene ("Main");
			else
				SceneManager.LoadScene ("Inside");
		}
	}
}