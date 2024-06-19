using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyScript : MonoBehaviour
{
    public GameObject shoot;
    float timer = 0f;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;
        if(timer > 2f){
            int sai = Random.Range(1, 7);
            if(sai == 1){
                Vector3 pos = transform.position - transform.up * 1.5f;
                Instantiate(shoot, pos, transform.rotation);
            }
            timer = 0f;
        }
    }
}
