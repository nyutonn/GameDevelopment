using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomScript : MonoBehaviour
{
    public GameObject coin;
    public GameObject fence;
    public GameObject turkey;
    // Start is called before the first frame update
    void Start()
    {
        //  ランダムに配置を決めるための座標
        int rnd = Random.Range(1, 4);
        if(rnd == 1){
            Instantiate(coin, transform.position + transform.right * 2, transform.rotation);
            Instantiate(fence, transform.position, transform.rotation);
            Instantiate(turkey, transform.position - transform.right * 2, transform.rotation);
        }
        else if(rnd == 2){
            Instantiate(fence, transform.position + transform.right * 2, transform.rotation);
            Instantiate(turkey, transform.position, transform.rotation);
            Instantiate(coin, transform.position - transform.right * 2, transform.rotation);
        }
        else if(rnd == 3){
            Instantiate(turkey, transform.position + transform.right * 2, transform.rotation);
            Instantiate(coin, transform.position, transform.rotation);
            Instantiate(fence, transform.position - transform.right * 2, transform.rotation);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
