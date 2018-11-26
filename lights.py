class Neon_Filter:
	#overlaying the filter to the video
	def overlay(self, frame, neon, pos=(0,0), scale = 1): 
		h, w, _ = neon.shape
		rows, cols, _ = frame.shape
		y, x = pos[0], pos[1]
		for n in range(h):
			for l in range(w):
				if x + n >= rows or y + l >= cols:
					continue
				alpha = float(neon[n][l][3] / 255.0)
				frame[x + n][y + l] = alpha * neon[n][l][:3] + (1 - alpha) * frame[x + n][y + l]
		return frame
