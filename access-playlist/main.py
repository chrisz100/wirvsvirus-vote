import random
from flask import redirect

playlists = [
    'PLYGe9q9_Jo3AhwDdN4qvhvqTSgfCdYRGD', 'PLYGe9q9_Jo3D4TkL-MqwldtfT6ycfH6hS', 'PLYGe9q9_Jo3DUa4uSGBqVIIufkOfUGgQT', 
    'PLYGe9q9_Jo3DmEkTT6FnNDwU1RFgfsCSS', 'PLYGe9q9_Jo3DGrwX_k5DQ9Ij-4QGHTCo2', 'PLYGe9q9_Jo3CAHYGb7eHLVl2YW4xFLPAM', 
    'PLYGe9q9_Jo3DDHG4zeyJOPcifV6K_ufvA', 'PLYGe9q9_Jo3BvYWODekJve315wqYJXck8', 'PLYGe9q9_Jo3DNrOVRMD6wXDXL1kypGLCQ', 
    'PLYGe9q9_Jo3CNYKF7CDzMbhMt_8zruJxs', 'PLYGe9q9_Jo3ArLqceUtXy1ATgk8CljR1W', 'PLYGe9q9_Jo3CBlvox5HpjT0g1Fq01GfyA', 
    'PLYGe9q9_Jo3DfGWYgATt4I0l1aJPotQD6', 'PLYGe9q9_Jo3BKjxYm6mVoJ7l6ZpAfGMq-', 'PLYGe9q9_Jo3DGsxXreqk2X8vd8HL0meBg', 
    'PLYGe9q9_Jo3BhYDGlqSE6qjRacC-5HTOs', 'PLYGe9q9_Jo3AyW9jBhib04Og0VJ1XugVW', 'PLYGe9q9_Jo3BRvZtPHutSZM_nt7sqHc7K', 
    'PLYGe9q9_Jo3DIjuX-K8YwaSLHMoHSwsTh', 'PLYGe9q9_Jo3CQ6VIoXw49eUp08Ehd-5QZ', 'PLYGe9q9_Jo3D6rxct6Bds6c8CQCqTucjd', 
    'PLYGe9q9_Jo3BKJEbGcWRFbngR1vb7BKkh', 'PLYGe9q9_Jo3A7caheWzc3UksSIkDFsAGQ', 'PLYGe9q9_Jo3BUpHe5ArxcXMiwOK_r_VMp', 
    'PLYGe9q9_Jo3B9L_1B5YKxHSabX1fgKpe-', 'PLYGe9q9_Jo3AoBNba-8YCx0scJIxG0sOW', 'PLYGe9q9_Jo3BKsarQfOkBgKdvDPnJNPwQ', 
    'PLYGe9q9_Jo3AZv0x4qX5ceGwZX8o0Svrd', 'PLYGe9q9_Jo3DTnfCl-t3LIYBA_prlY2YP', 'PLYGe9q9_Jo3CW35KIX9sh1Ky-qX7TTh0a', 
    'PLYGe9q9_Jo3CiB_2nGCz2x9wqobYCjVd1', 'PLYGe9q9_Jo3BQHLIYrQR2qNnCQ_LdVL_e', 'PLYGe9q9_Jo3AayDdJK-C0m8nt6bz7URQL', 
    'PLYGe9q9_Jo3AMh2Fc3tuqskbNxnEbtNSk', 'PLYGe9q9_Jo3AAEKDD9zj2bfyV6mPVjM3k', 'PLYGe9q9_Jo3AWQ-yrg3XfLTmqUNEwRZCd', 
    'PLYGe9q9_Jo3A8pMFE0qlS-PKyDP5ROrae', 'PLYGe9q9_Jo3CzAB7Ubmya4zTpIjQg-4-u', 'PLYGe9q9_Jo3A0WfDG2QgMchgpUjAyzPty', 
    'PLYGe9q9_Jo3B34fBh2vurqQOrH6OyKZT4', 'PLYGe9q9_Jo3BZrGW5wS7tUiKE6hNhfeuN', 'PLYGe9q9_Jo3CbG1NUAa1kGg53no1bymTp', 
    'PLYGe9q9_Jo3CX_inSvwRz3KUq6xUzrJk7', 'PLYGe9q9_Jo3CRKfRRmXBQtwZWcrQxFtk6', 'PLYGe9q9_Jo3CQHr_5TJh1D0MFmAm-j4MP', 
    'PLYGe9q9_Jo3ChycPu3bJWo1nud3vImzas', 'PLYGe9q9_Jo3Ck3IZiougPoG3DKaA4lRd7', 'PLYGe9q9_Jo3CLwsE6WLSZ1GDQfUSc0jpw', 
    'PLYGe9q9_Jo3B8RpljWkafo4A_Iyydcod0', 'PLYGe9q9_Jo3CyLm4If21uC0Run9F2v5RF', 'PLYGe9q9_Jo3ChxzxKj5wXo_K6svw52YDe', 
    'PLYGe9q9_Jo3AGOtBgb7imt8QBIh0sxGFG', 'PLYGe9q9_Jo3D1zY8YMY7zkP1pfwJMTC0-', 'PLYGe9q9_Jo3D066pjI3yfSPzU9sFuGz2F', 
    'PLYGe9q9_Jo3CHeMpizjilx_MQdt6JbC74', 'PLYGe9q9_Jo3DLXcV4N9yMXRapzqBafyUk', 'PLYGe9q9_Jo3BVJTDAeSf1eLYWQ9NsC-BB', 
    'PLYGe9q9_Jo3BxQpBzeWalYw10dHJctKsi', 'PLYGe9q9_Jo3ACPrLl254tFn534_Isl0Ld', 'PLYGe9q9_Jo3BSohTV5TwxTDZ9RIIY1eBb', 
    'PLYGe9q9_Jo3DXJ-RYxDzA-K5LEiFkRWfB', 'PLYGe9q9_Jo3DV5QGxV7dTTfZHAy85scKn', 'PLYGe9q9_Jo3CUECyzHlPPPjeGdRYT6Dx4', 
    'PLYGe9q9_Jo3DUBUl3shGVEIX_6Kz25cLa', 'PLYGe9q9_Jo3AzGEqR41Q-74nZvVZBz6DX', 'PLYGe9q9_Jo3Ci-vAc6qTkczkPZVOx2pcT', 
    'PLYGe9q9_Jo3AP2Sde93VOZVgW8fNk9t0n', 'PLYGe9q9_Jo3CNGrJc-8ecGBvOaVRZUsGr', 'PLYGe9q9_Jo3B1nLc532mOEDw7zbg2g_nr', 
    'PLYGe9q9_Jo3Ct7zoDLU-sXY7HiJ8sOlLD', 'PLYGe9q9_Jo3D7xOGBRw2333974jXu9TtW', 'PLYGe9q9_Jo3BYazUICklbO4r0SzppsR_D', 
    'PLYGe9q9_Jo3A2dQPWATTUtxGtS4ppaUE2', 'PLYGe9q9_Jo3BcnRNA1be5R8Z4U1XNPSFJ', 'PLYGe9q9_Jo3C9VkvYLoK5mPpV4wxMnZtB', 
    'PLYGe9q9_Jo3AyFv1GRd0QQ_XISJ2wb_ci', 'PLYGe9q9_Jo3Bg2IKUDqoKNWslfFi78H9T', 'PLYGe9q9_Jo3DbuIp6SDV6HKtIiHtl934S', 
    'PLYGe9q9_Jo3DVkrZTVolQ_WQhGwpiOv9F', 'PLYGe9q9_Jo3A5VStACbyldvGgi_Q9YWp6', 'PLYGe9q9_Jo3AM5KDN4ikS5s2rZl-RV3nF', 
    'PLYGe9q9_Jo3BTDgsp_hphvnDa3eaoHa1e', 'PLYGe9q9_Jo3Cgn5l0t-8gDiWQmKobIVnB', 'PLYGe9q9_Jo3AA7HPqMp6YU9rujL87htJm', 
    'PLYGe9q9_Jo3DNQSsWAydC-0xdbX8Aup2s', 'PLYGe9q9_Jo3BqcFG3dGgALZoyHLN44Dil', 'PLYGe9q9_Jo3Dsb7vUwa1EX7ikorORjlHC', 
    'PLYGe9q9_Jo3DFGCBVv2Z5D5PDS5tFEyvB', 'PLYGe9q9_Jo3ArBCSPokupKNVQscpbE0yW', 'PLYGe9q9_Jo3ALtXvFy8-IhOl7mmlmjvRU', 
    'PLYGe9q9_Jo3AsE3fab299dkQ1SgC6nyyN', 'PLYGe9q9_Jo3COW8jGZJPCrck0kteZjPus', 'PLYGe9q9_Jo3C7CIxc0lC80LKh21gXQN3_', 
    'PLYGe9q9_Jo3Bn3MvLbcRYBnHfo4f4Vvem', 'PLYGe9q9_Jo3D_Pq4PVnn9KM-TClBWJg8R', 'PLYGe9q9_Jo3DCd4Dfgr4Vgf0d1MqMdjnM', 
    'PLYGe9q9_Jo3ByR15gnAtXc5JSmifen22k', 'PLYGe9q9_Jo3CVCmxLdq2NLlF7Oo2gCb7m', 'PLYGe9q9_Jo3DakGvWcb-rZPLtrUOe3Lox', 
    'PLYGe9q9_Jo3DLCGmfqlIyPo85kVS_TPQJ'
]

def random_video(request):
    try:
        playlist = playlists[random.randrange(0, len(playlists))]
        return redirect(f'https://www.youtube.com/playlist?list={playlist}')
    except:
        return f'Playlist not found'
