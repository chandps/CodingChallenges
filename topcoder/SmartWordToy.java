public class SmartWordToy {
  int qs;
  int qe;
  int[] buf = new int[4];

  public int minPresses(String start, String finish, String[] forbid) {
    boolean[] forb = new boolean[26 * 26 * 26 * 26];
    int[] q = new int[26 * 26 * 26 * 26 + 5];
    int[] stepCount = new int[26 * 26 * 26 * 26 + 5];
    boolean[] vis = new boolean[26 * 26 * 26 * 26 + 5];
    qe = qs = 0;

    for (int i = 0; i < forbid.length; ++i) {
      String s = forbid[i];
      String[] strings = s.split(" ");
      for (int i1 = 0; i1 < strings[0].length(); ++i1) {
        int c1 = strings[0].charAt(i1);
        for (int i2 = 0; i2 < strings[1].length(); ++i2) {
          int c2 = strings[1].charAt(i2);
          for (int i3 = 0; i3 < strings[2].length(); ++i3) {
            int c3 = strings[2].charAt(i3);
            for (int i4 = 0; i4 < strings[3].length(); ++i4) {
                     int c4 = strings[3].charAt(i4);
              int code = ((c1 - 'a') * 26 * 26 * 26) +
                      ((c2 - 'a') * 26 * 26) +
                      ((c3 - 'a') * 26) + ((c4 - 'a'));
              forb[code] = true;
            }
          }
        }
      }
    }

    int st = code(start);
    int fin = code(finish);

    if (forb[st] || forb[fin]) {
      return -1;
    }

    int[] temp = new int[4];

    q[qe++] = st;
    vis[st] = true;
    while (qs < qe) {
      int step = stepCount[qs];
      int v = q[qs++];
      if (v == fin) {
        return stepCount[qs - 1];
      }

      temp[3] = v % 26;
      v /= 26;
      temp[2] = v % 26;
      v /= 26;
      temp[1] = v % 26;
      v /= 26;
      temp[0] = v % 26;

      for (int k = 0; k < 4; ++k) {
        for (int b = 0; b < 2; ++b) {
          next(k, b == 0, temp);
          int n = buf[0] * 26 * 26 * 26 + buf[1] * 26 * 26 + buf[2] * 26 + buf[3];
          if (!vis[n] && !forb[n]) {
            vis[n] = true;
            stepCount[qe] = step + 1;
            q[qe++] = n;
          }
        }
      }
    }

    return -1;
  }


  void next(int pos, boolean up, int[] t) {
    buf[0] = t[0];
    buf[1] = t[1];
    buf[2] = t[2];
    buf[3] = t[3];

    if (up) {
      if (++buf[pos] == 26) buf[pos] = 0;
    } else {
      if (--buf[pos] == -1) buf[pos] = 25;
    }
  }

  int code (String s) {
    return ((s.charAt(0) - 'a') * 26 * 26 * 26) +
         ((s.charAt(1) - 'a') * 26 * 26) +
         ((s.charAt(2) - 'a') * 26) + ((s.charAt(3) - 'a'));
  }


}
