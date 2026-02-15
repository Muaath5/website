/**
 * Reading Time Estimator
 * Handles both Arabic (RTL) and English (LTR) content.
 *
 * Arabic average reading speed: ~138 wpm (research suggests slightly
 * slower than English due to diacritics and morphological density).
 * English average reading speed: ~200 wpm.
 * Code blocks: counted at ~50 wpm equivalent.
 */
(function () {
    'use strict';

    var WPM_AR = 138;
    var WPM_EN = 200;
    var WPM_CODE = 50;

    var article = document.getElementById('post-content');
    var badge   = document.getElementById('reading-time-text');
    if (!article || !badge) return;

    var lang = document.documentElement.lang || 'en';
    var wpm  = lang === 'ar' ? WPM_AR : WPM_EN;

    // Extract text content (excluding code blocks)
    var clone = article.cloneNode(true);

    // Count code words separately
    var codeBlocks = clone.querySelectorAll('pre, code');
    var codeWords  = 0;
    for (var i = 0; i < codeBlocks.length; i++) {
        codeWords += codeBlocks[i].textContent.trim().split(/\s+/).filter(Boolean).length;
        codeBlocks[i].textContent = '';
    }

    // Count remaining (prose) words
    var text = clone.textContent || '';
    var proseWords = text.trim().split(/\s+/).filter(Boolean).length;

    // Calculate total reading time
    var minutes = Math.ceil(proseWords / wpm + codeWords / WPM_CODE);
    if (minutes < 1) minutes = 1;

    // Display
    if (lang === 'ar') {
        if (minutes === 1) {
            badge.textContent = 'دقيقة واحدة للقراءة';
        } else if (minutes === 2) {
            badge.textContent = 'دقيقتان للقراءة';
        } else if (minutes <= 10) {
            badge.textContent = minutes + ' دقائق للقراءة';
        } else {
            badge.textContent = minutes + ' دقيقة للقراءة';
        }
    } else {
        badge.textContent = minutes + ' min read';
    }
})();