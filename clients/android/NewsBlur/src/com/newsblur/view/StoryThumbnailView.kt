package com.newsblur.view

import android.content.Context
import android.util.AttributeSet
import androidx.appcompat.widget.AppCompatImageView
import com.newsblur.R
import com.newsblur.util.ThumbnailStyle

class StoryThumbnailView
@JvmOverloads constructor(context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0)
    : AppCompatImageView(context, attrs, defStyleAttr) {

    init {
        clipToOutline = true
        scaleType = ScaleType.CENTER_CROP
    }

    fun setThumbnailStyle(thumbnailStyle: ThumbnailStyle) {
        if (thumbnailStyle == ThumbnailStyle.LEFT_SMALL || thumbnailStyle == ThumbnailStyle.RIGHT_SMALL) {
            setBackgroundResource(R.drawable.shape_rounded_corners)
        } else {
            setBackgroundResource(0)
        }
    }
}