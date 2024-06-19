using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class hatenaScript : MonoBehaviour
{
    public GameObject coincoin;
    public AudioSource aus; // 自身の名前
    public AudioClip coin; // SE
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void playMusic(){
        aus.clip = coin;
        aus.Play();
        Debug.Log("coin");
        create_coin();
    }
    void create_coin(){
        Vector3 pos = new Vector3(0f, 3f, -3);
        Vector3 rot = new Vector3(90f, 0f, 0f);
        Instantiate(coincoin, pos, transform.rotation);
    }
}
