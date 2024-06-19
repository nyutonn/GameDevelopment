using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    private Camera MainCam;
    public float DPIX = 1.0f;
    public float DPIY = 1.0f;
    public float MoveSpeed = 0.01f;
    // Start is called before the first frame update
    void Start()
    {
        MainCam = Camera.main;
        Cursor.lockState = CursorLockMode.Locked;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Cursor.lockState = CursorLockMode.None;
        }
        float mousex = Input.GetAxis("Mouse X");
        float mousey = Input.GetAxis("Mouse Y");
        transform.Rotate(0f, mousex * DPIX, 0f);
        MainCam.transform.Rotate(mousey * DPIY, 0f, 0f);

        //‰¡–îˆó“ü—Í‚ğ’l‚Å•Ô‚µ•Ï”uHorizontalv‚ÉŠi”[
        float Horizontal = Input.GetAxis("Horizontal");
        //c–îˆó“ü—Í‚ğ’l‚Å•Ô‚µ•Ï”uVerticalv‚ÉŠi”[
        float Vertical = Input.GetAxis("Vertical");
        //‚±‚Ì‚Ü‚Ü“ü‚ê‚é‚Æ‘‚·‚¬‚éˆ×MoveSpeed‚Å’²®
        transform.position += transform.right * Horizontal * MoveSpeed;
        transform.position += transform.forward * Vertical * MoveSpeed;
    }
}
