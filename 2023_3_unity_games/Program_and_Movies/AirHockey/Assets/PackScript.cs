using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PackScript : MonoBehaviour
{
    public Rigidbody rb;
    int scoreRed = 0;
    int scoreBlue = 0;
    public Text scoreText;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        scoreText.text = scoreRed + " : " + scoreBlue;
    }

    void OnTriggerEnter(Collider other){
        if(other.gameObject.CompareTag("Red")){
            transform.position = new Vector3(0f, -9f, -10f);
            rb.velocity = new Vector3(0f, 0f ,0f);
            scoreRed += 1;
        }
        if(other.gameObject.CompareTag("Blue")){
            transform.position = new Vector3(0f, -9f, -10f);
            rb.velocity = new Vector3(0f, 0f ,0f);
            scoreBlue += 1;
        }
    }
}
